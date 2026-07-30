from __future__ import annotations

import csv
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Final


APP_NAME: Final[str] = "INVENTORY MANAGEMENT SYSTEM"
BASE_DIR: Final[Path] = Path(__file__).resolve().parent
DATABASE_FILE: Final[Path] = BASE_DIR / "database" / "inventory.db"
EXPORT_DIR: Final[Path] = BASE_DIR / "exports"
DATE_TIME_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
DISPLAY_DATE_TIME_FORMAT: Final[str] = "%d-%m-%Y %I:%M %p"


@dataclass(frozen=True, slots=True)
class Product:
    """Represent one inventory product."""

    product_id: int
    sku: str
    name: str
    category: str
    unit_price: Decimal
    quantity: int
    reorder_level: int
    supplier: str
    created_at: str
    updated_at: str


def as_money(value: str | int | float | Decimal) -> Decimal:
    """Convert a value to a two-decimal Decimal."""

    return Decimal(str(value)).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP,
    )


def format_currency(value: str | int | float | Decimal) -> str:
    """Format a value as Indian currency."""

    return f"₹{as_money(value):,.2f}"


def format_datetime(value: str) -> str:
    """Format a database timestamp for terminal display."""

    try:
        parsed = datetime.strptime(value, DATE_TIME_FORMAT)
        return parsed.strftime(DISPLAY_DATE_TIME_FORMAT)
    except ValueError:
        return value


def shorten(value: str, size: int) -> str:
    """Shorten long text for table output."""

    return value if len(value) <= size else value[: size - 3] + "..."


def heading(title: str, width: int = 88) -> None:
    """Print a formatted heading."""

    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def pause() -> None:
    """Pause until the user presses Enter."""

    input("\nPress Enter to continue...")


def get_required_text(prompt: str) -> str:
    """Receive a required text value."""

    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_integer(
    prompt: str,
    minimum: int = 0,
    maximum: int | None = None,
    default: int | None = None,
) -> int:
    """Receive and validate an integer."""

    while True:
        value = input(prompt).strip()

        if not value and default is not None:
            return default

        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if number < minimum:
            print(f"Enter a number greater than or equal to {minimum}.")
            continue

        if maximum is not None and number > maximum:
            print(f"Enter a number less than or equal to {maximum}.")
            continue

        return number


def get_decimal(
    prompt: str,
    minimum: Decimal = Decimal("0.00"),
    default: Decimal | None = None,
) -> Decimal:
    """Receive and validate a decimal amount."""

    while True:
        value = input(prompt).strip()

        if not value and default is not None:
            return default

        try:
            amount = as_money(value)
        except (InvalidOperation, ValueError):
            print("Enter a valid amount, for example 199.99.")
            continue

        if amount < minimum:
            print(f"Amount must be at least {format_currency(minimum)}.")
            continue

        return amount


def get_yes_no(prompt: str, default: bool | None = None) -> bool:
    """Receive and validate a yes-or-no response."""

    while True:
        value = input(prompt).strip().lower()

        if not value and default is not None:
            return default
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False

        print("Please enter y for yes or n for no.")


def connection() -> sqlite3.Connection:
    """Create and configure a SQLite connection."""

    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DATABASE_FILE)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db


def initialize_database() -> None:
    """Create the database schema."""

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    with connection() as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT NOT NULL UNIQUE COLLATE NOCASE,
                name TEXT NOT NULL COLLATE NOCASE,
                category TEXT NOT NULL COLLATE NOCASE,
                unit_price TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0),
                reorder_level INTEGER NOT NULL DEFAULT 5
                    CHECK(reorder_level >= 0),
                supplier TEXT NOT NULL COLLATE NOCASE,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS stock_movements (
                movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                movement_type TEXT NOT NULL CHECK(
                    movement_type IN ('INITIAL', 'RESTOCK', 'SALE', 'ADJUSTMENT')
                ),
                quantity_change INTEGER NOT NULL,
                previous_quantity INTEGER NOT NULL,
                new_quantity INTEGER NOT NULL,
                notes TEXT NOT NULL DEFAULT '',
                movement_at TEXT NOT NULL,
                FOREIGN KEY(product_id)
                    REFERENCES products(product_id)
                    ON DELETE RESTRICT
            );

            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity_sold INTEGER NOT NULL CHECK(quantity_sold > 0),
                unit_price TEXT NOT NULL,
                total_amount TEXT NOT NULL,
                sold_at TEXT NOT NULL,
                FOREIGN KEY(product_id)
                    REFERENCES products(product_id)
                    ON DELETE RESTRICT
            );

            CREATE INDEX IF NOT EXISTS idx_products_name
            ON products(name);

            CREATE INDEX IF NOT EXISTS idx_products_category
            ON products(category);
            """
        )


def product_from_row(row: sqlite3.Row) -> Product:
    """Convert a database row to a Product."""

    return Product(
        product_id=int(row["product_id"]),
        sku=str(row["sku"]),
        name=str(row["name"]),
        category=str(row["category"]),
        unit_price=as_money(row["unit_price"]),
        quantity=int(row["quantity"]),
        reorder_level=int(row["reorder_level"]),
        supplier=str(row["supplier"]),
        created_at=str(row["created_at"]),
        updated_at=str(row["updated_at"]),
    )


def find_product(identifier: str) -> Product | None:
    """Find a product by product ID or SKU."""

    identifier = identifier.strip()

    with connection() as db:
        if identifier.isdigit():
            row = db.execute(
                "SELECT * FROM products WHERE product_id = ?",
                (int(identifier),),
            ).fetchone()
        else:
            row = db.execute(
                "SELECT * FROM products WHERE sku = ? COLLATE NOCASE",
                (identifier,),
            ).fetchone()

    return product_from_row(row) if row else None


def request_product() -> Product | None:
    """Ask for a product ID or SKU and return the matching product."""

    identifier = get_required_text("Enter product ID or SKU: ")
    return find_product(identifier)


def record_movement(
    db: sqlite3.Connection,
    product_id: int,
    movement_type: str,
    quantity_change: int,
    previous_quantity: int,
    new_quantity: int,
    notes: str,
    timestamp: str,
) -> None:
    """Insert a stock movement inside an existing transaction."""

    db.execute(
        """
        INSERT INTO stock_movements (
            product_id,
            movement_type,
            quantity_change,
            previous_quantity,
            new_quantity,
            notes,
            movement_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            product_id,
            movement_type,
            quantity_change,
            previous_quantity,
            new_quantity,
            notes,
            timestamp,
        ),
    )


def add_product() -> None:
    """Add a product to inventory."""

    heading("ADD PRODUCT")

    sku = get_required_text("SKU: ").upper()

    if find_product(sku):
        print("\nA product with this SKU already exists.")
        return

    name = get_required_text("Product name: ").title()
    category = get_required_text("Category: ").title()
    price = get_decimal("Unit price: ", Decimal("0.01"))
    quantity = get_integer("Opening quantity: ", minimum=0)
    reorder_level = get_integer(
        "Reorder level [default 5]: ",
        minimum=0,
        default=5,
    )
    supplier = get_required_text("Supplier: ").title()
    timestamp = datetime.now().strftime(DATE_TIME_FORMAT)

    try:
        with connection() as db:
            cursor = db.execute(
                """
                INSERT INTO products (
                    sku,
                    name,
                    category,
                    unit_price,
                    quantity,
                    reorder_level,
                    supplier,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    sku,
                    name,
                    category,
                    str(price),
                    quantity,
                    reorder_level,
                    supplier,
                    timestamp,
                    timestamp,
                ),
            )

            product_id = int(cursor.lastrowid)

            record_movement(
                db,
                product_id,
                "INITIAL",
                quantity,
                0,
                quantity,
                "Opening stock",
                timestamp,
            )
    except sqlite3.IntegrityError:
        print("\nUnable to add the product because the SKU already exists.")
        return
    except sqlite3.Error as error:
        print(f"\nDatabase error: {error}")
        return

    print(f"\nProduct added successfully with ID {product_id}.")


def all_products() -> list[Product]:
    """Return every product sorted by name."""

    with connection() as db:
        rows = db.execute(
            "SELECT * FROM products ORDER BY name COLLATE NOCASE"
        ).fetchall()

    return [product_from_row(row) for row in rows]


def display_products(products: list[Product]) -> None:
    """Display products in a table."""

    if not products:
        print("\nNo products found.")
        return

    print(
        f"\n{'ID':<6}"
        f"{'SKU':<13}"
        f"{'Product':<24}"
        f"{'Category':<17}"
        f"{'Price':>13}"
        f"{'Qty':>7}"
        f"{'Status':>12}"
    )
    print("-" * 92)

    for product in products:
        status = (
            "LOW STOCK"
            if product.quantity <= product.reorder_level
            else "In Stock"
        )

        print(
            f"{product.product_id:<6}"
            f"{shorten(product.sku, 11):<13}"
            f"{shorten(product.name, 22):<24}"
            f"{shorten(product.category, 15):<17}"
            f"{format_currency(product.unit_price):>13}"
            f"{product.quantity:>7}"
            f"{status:>12}"
        )

    print("-" * 92)
    print(f"Total products: {len(products)}")


def view_products() -> None:
    """Display all products."""

    heading("ALL PRODUCTS")
    display_products(all_products())


def search_products() -> None:
    """Search products by ID, SKU, name, category or supplier."""

    heading("SEARCH PRODUCTS")
    keyword = get_required_text(
        "Enter ID, SKU, name, category or supplier: "
    )
    like_value = f"%{keyword}%"

    with connection() as db:
        rows = db.execute(
            """
            SELECT *
            FROM products
            WHERE CAST(product_id AS TEXT) LIKE ?
               OR sku LIKE ? COLLATE NOCASE
               OR name LIKE ? COLLATE NOCASE
               OR category LIKE ? COLLATE NOCASE
               OR supplier LIKE ? COLLATE NOCASE
            ORDER BY name COLLATE NOCASE
            """,
            (
                like_value,
                like_value,
                like_value,
                like_value,
                like_value,
            ),
        ).fetchall()

    display_products([product_from_row(row) for row in rows])


def update_product() -> None:
    """Update product details."""

    heading("UPDATE PRODUCT")
    product = request_product()

    if product is None:
        print("\nProduct not found.")
        return

    print("\nPress Enter to keep an existing value.")

    sku_input = input(f"SKU [{product.sku}]: ").strip().upper()
    new_sku = sku_input or product.sku

    existing = find_product(new_sku)
    if existing and existing.product_id != product.product_id:
        print("\nAnother product already uses this SKU.")
        return

    name = input(f"Product name [{product.name}]: ").strip()
    category = input(f"Category [{product.category}]: ").strip()
    supplier = input(f"Supplier [{product.supplier}]: ").strip()

    new_name = name.title() if name else product.name
    new_category = category.title() if category else product.category
    new_supplier = supplier.title() if supplier else product.supplier

    new_price = get_decimal(
        f"Unit price [{product.unit_price}]: ",
        Decimal("0.01"),
        product.unit_price,
    )
    new_reorder_level = get_integer(
        f"Reorder level [{product.reorder_level}]: ",
        minimum=0,
        default=product.reorder_level,
    )
    timestamp = datetime.now().strftime(DATE_TIME_FORMAT)

    try:
        with connection() as db:
            db.execute(
                """
                UPDATE products
                SET sku = ?,
                    name = ?,
                    category = ?,
                    unit_price = ?,
                    reorder_level = ?,
                    supplier = ?,
                    updated_at = ?
                WHERE product_id = ?
                """,
                (
                    new_sku,
                    new_name,
                    new_category,
                    str(new_price),
                    new_reorder_level,
                    new_supplier,
                    timestamp,
                    product.product_id,
                ),
            )
    except sqlite3.IntegrityError:
        print("\nUnable to update because the SKU is already in use.")
        return
    except sqlite3.Error as error:
        print(f"\nDatabase error: {error}")
        return

    print("\nProduct updated successfully.")


def adjust_stock() -> None:
    """Set a product's quantity to a corrected value."""

    heading("ADJUST STOCK")
    product = request_product()

    if product is None:
        print("\nProduct not found.")
        return

    print(f"\nCurrent quantity: {product.quantity}")
    new_quantity = get_integer("Correct quantity: ", minimum=0)

    if new_quantity == product.quantity:
        print("\nThe entered quantity is already current.")
        return

    notes = get_required_text("Reason for adjustment: ")
    change = new_quantity - product.quantity
    timestamp = datetime.now().strftime(DATE_TIME_FORMAT)

    try:
        with connection() as db:
            db.execute(
                """
                UPDATE products
                SET quantity = ?, updated_at = ?
                WHERE product_id = ?
                """,
                (new_quantity, timestamp, product.product_id),
            )

            record_movement(
                db,
                product.product_id,
                "ADJUSTMENT",
                change,
                product.quantity,
                new_quantity,
                notes,
                timestamp,
            )
    except sqlite3.Error as error:
        print(f"\nDatabase error: {error}")
        return

    print("\nStock adjusted successfully.")


def delete_product() -> None:
    """Delete a product that has no sales history."""

    heading("DELETE PRODUCT")
    product = request_product()

    if product is None:
        print("\nProduct not found.")
        return

    with connection() as db:
        sales_count = int(
            db.execute(
                "SELECT COUNT(*) FROM sales WHERE product_id = ?",
                (product.product_id,),
            ).fetchone()[0]
        )

    if sales_count:
        print(
            "\nThis product cannot be deleted because it has sales history."
        )
        return

    print(f"\nProduct: {product.name} ({product.sku})")

    if not get_yes_no("Delete this product? (y/N): ", default=False):
        print("\nDeletion cancelled.")
        return

    try:
        with connection() as db:
            db.execute(
                "DELETE FROM stock_movements WHERE product_id = ?",
                (product.product_id,),
            )
            db.execute(
                "DELETE FROM products WHERE product_id = ?",
                (product.product_id,),
            )
    except sqlite3.Error as error:
        print(f"\nDatabase error: {error}")
        return

    print("\nProduct deleted successfully.")


def product_menu() -> None:
    """Display product-management options."""

    while True:
        heading("PRODUCT MANAGEMENT")
        print("1. Add product")
        print("2. View all products")
        print("3. Search products")
        print("4. Update product")
        print("5. Adjust stock")
        print("6. Delete product")
        print("7. Back to main menu")

        choice = input("\nChoose an option from 1 to 7: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_products()
        elif choice == "4":
            update_product()
        elif choice == "5":
            adjust_stock()
        elif choice == "6":
            delete_product()
        elif choice == "7":
            return
        else:
            print("\nInvalid option. Choose a number from 1 to 7.")

        pause()


def restock_product() -> None:
    """Increase the available stock of a product."""

    heading("RESTOCK PRODUCT")
    product = request_product()

    if product is None:
        print("\nProduct not found.")
        return

    print(f"\nProduct         : {product.name}")
    print(f"Current quantity: {product.quantity}")

    quantity_added = get_integer("Quantity to add: ", minimum=1)
    notes = input("Restock note [optional]: ").strip() or "Product restocked"
    new_quantity = product.quantity + quantity_added
    timestamp = datetime.now().strftime(DATE_TIME_FORMAT)

    try:
        with connection() as db:
            db.execute(
                """
                UPDATE products
                SET quantity = ?, updated_at = ?
                WHERE product_id = ?
                """,
                (new_quantity, timestamp, product.product_id),
            )

            record_movement(
                db,
                product.product_id,
                "RESTOCK",
                quantity_added,
                product.quantity,
                new_quantity,
                notes,
                timestamp,
            )
    except sqlite3.Error as error:
        print(f"\nDatabase error: {error}")
        return

    print("\nProduct restocked successfully.")
    print(f"New quantity: {new_quantity}")


def record_sale() -> None:
    """Record a sale and reduce stock."""

    heading("RECORD SALE")
    product = request_product()

    if product is None:
        print("\nProduct not found.")
        return

    if product.quantity == 0:
        print("\nThis product is out of stock.")
        return

    print(f"\nProduct    : {product.name}")
    print(f"Available  : {product.quantity}")
    print(f"Unit price : {format_currency(product.unit_price)}")

    quantity_sold = get_integer(
        "Quantity sold: ",
        minimum=1,
        maximum=product.quantity,
    )
    total = as_money(product.unit_price * quantity_sold)

    print(f"Total      : {format_currency(total)}")

    if not get_yes_no("Confirm sale? (Y/n): ", default=True):
        print("\nSale cancelled.")
        return

    new_quantity = product.quantity - quantity_sold
    timestamp = datetime.now().strftime(DATE_TIME_FORMAT)

    try:
        with connection() as db:
            db.execute(
                """
                INSERT INTO sales (
                    product_id,
                    quantity_sold,
                    unit_price,
                    total_amount,
                    sold_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    product.product_id,
                    quantity_sold,
                    str(product.unit_price),
                    str(total),
                    timestamp,
                ),
            )

            db.execute(
                """
                UPDATE products
                SET quantity = ?, updated_at = ?
                WHERE product_id = ?
                """,
                (new_quantity, timestamp, product.product_id),
            )

            record_movement(
                db,
                product.product_id,
                "SALE",
                -quantity_sold,
                product.quantity,
                new_quantity,
                "Product sale",
                timestamp,
            )
    except sqlite3.Error as error:
        print(f"\nDatabase error: {error}")
        return

    print("\nSale recorded successfully.")
    print(f"Remaining stock: {new_quantity}")


def view_sales() -> None:
    """Display complete sales history."""

    heading("SALES HISTORY", width=105)

    with connection() as db:
        rows = db.execute(
            """
            SELECT
                s.sale_id,
                p.sku,
                p.name,
                s.quantity_sold,
                s.unit_price,
                s.total_amount,
                s.sold_at
            FROM sales AS s
            JOIN products AS p
              ON p.product_id = s.product_id
            ORDER BY s.sale_id DESC
            """
        ).fetchall()

    if not rows:
        print("\nNo sales found.")
        return

    print(
        f"\n{'Sale ID':<9}"
        f"{'SKU':<13}"
        f"{'Product':<26}"
        f"{'Qty':>7}"
        f"{'Unit Price':>15}"
        f"{'Total':>15}"
        f"{'Sold At':>21}"
    )
    print("-" * 106)

    for row in rows:
        print(
            f"{int(row['sale_id']):<9}"
            f"{shorten(str(row['sku']), 11):<13}"
            f"{shorten(str(row['name']), 24):<26}"
            f"{int(row['quantity_sold']):>7}"
            f"{format_currency(row['unit_price']):>15}"
            f"{format_currency(row['total_amount']):>15}"
            f"{format_datetime(str(row['sold_at'])):>21}"
        )

    print("-" * 106)


def stock_sales_menu() -> None:
    """Display stock and sales options."""

    while True:
        heading("STOCK AND SALES")
        print("1. Restock product")
        print("2. Record sale")
        print("3. View sales history")
        print("4. Back to main menu")

        choice = input("\nChoose an option from 1 to 4: ").strip()

        if choice == "1":
            restock_product()
        elif choice == "2":
            record_sale()
        elif choice == "3":
            view_sales()
        elif choice == "4":
            return
        else:
            print("\nInvalid option. Choose a number from 1 to 4.")

        pause()


def inventory_summary() -> None:
    """Display important inventory statistics."""

    heading("INVENTORY SUMMARY")

    products = all_products()

    with connection() as db:
        sales = db.execute(
            """
            SELECT
                COALESCE(SUM(quantity_sold), 0) AS units_sold,
                COALESCE(SUM(CAST(total_amount AS REAL)), 0) AS revenue
            FROM sales
            """
        ).fetchone()

    product_count = len(products)
    total_units = sum(product.quantity for product in products)
    low_stock_count = sum(
        product.quantity <= product.reorder_level for product in products
    )
    inventory_value = sum(
        product.unit_price * product.quantity for product in products
    )

    print(f"{'Number of products':<40}{product_count:>18}")
    print(f"{'Total units in stock':<40}{total_units:>18}")
    print(f"{'Low-stock products':<40}{low_stock_count:>18}")
    print(f"{'Inventory value':<40}{format_currency(inventory_value):>18}")
    print(f"{'Total units sold':<40}{int(sales['units_sold']):>18}")
    print(
        f"{'Total sales revenue':<40}"
        f"{format_currency(sales['revenue']):>18}"
    )


def low_stock_report() -> None:
    """Display products that require restocking."""

    heading("LOW-STOCK REPORT")

    with connection() as db:
        rows = db.execute(
            """
            SELECT *
            FROM products
            WHERE quantity <= reorder_level
            ORDER BY quantity, name COLLATE NOCASE
            """
        ).fetchall()

    products = [product_from_row(row) for row in rows]

    if not products:
        print("\nAll products are above their reorder levels.")
        return

    print(
        f"\n{'ID':<6}"
        f"{'SKU':<13}"
        f"{'Product':<27}"
        f"{'Supplier':<23}"
        f"{'Qty':>8}"
        f"{'Reorder':>10}"
    )
    print("-" * 87)

    for product in products:
        print(
            f"{product.product_id:<6}"
            f"{shorten(product.sku, 11):<13}"
            f"{shorten(product.name, 25):<27}"
            f"{shorten(product.supplier, 21):<23}"
            f"{product.quantity:>8}"
            f"{product.reorder_level:>10}"
        )

    print("-" * 87)


def category_report() -> None:
    """Display stock grouped by category."""

    heading("CATEGORY REPORT")
    products = all_products()

    if not products:
        print("\nNo products found.")
        return

    categories: dict[str, dict[str, Decimal | int]] = {}

    for product in products:
        details = categories.setdefault(
            product.category,
            {
                "product_count": 0,
                "units": 0,
                "value": Decimal("0.00"),
            },
        )
        details["product_count"] += 1
        details["units"] += product.quantity
        details["value"] += product.unit_price * product.quantity

    print(
        f"\n{'Category':<29}"
        f"{'Products':>12}"
        f"{'Units':>12}"
        f"{'Stock Value':>20}"
    )
    print("-" * 73)

    for category in sorted(categories, key=str.casefold):
        details = categories[category]
        print(
            f"{shorten(category, 27):<29}"
            f"{int(details['product_count']):>12}"
            f"{int(details['units']):>12}"
            f"{format_currency(details['value']):>20}"
        )

    print("-" * 73)


def top_selling_report() -> None:
    """Display products ranked by quantity sold."""

    heading("TOP-SELLING PRODUCTS")

    with connection() as db:
        rows = db.execute(
            """
            SELECT
                p.sku,
                p.name,
                SUM(s.quantity_sold) AS units_sold,
                SUM(CAST(s.total_amount AS REAL)) AS revenue
            FROM sales AS s
            JOIN products AS p
              ON p.product_id = s.product_id
            GROUP BY p.product_id, p.sku, p.name
            ORDER BY units_sold DESC, revenue DESC
            LIMIT 10
            """
        ).fetchall()

    if not rows:
        print("\nNo sales data is available.")
        return

    print(
        f"\n{'Rank':<8}"
        f"{'SKU':<14}"
        f"{'Product':<34}"
        f"{'Units Sold':>14}"
        f"{'Revenue':>18}"
    )
    print("-" * 88)

    for rank, row in enumerate(rows, start=1):
        print(
            f"{rank:<8}"
            f"{shorten(str(row['sku']), 12):<14}"
            f"{shorten(str(row['name']), 32):<34}"
            f"{int(row['units_sold']):>14}"
            f"{format_currency(row['revenue']):>18}"
        )

    print("-" * 88)


def movement_history() -> None:
    """Display complete stock movement history."""

    heading("STOCK MOVEMENT HISTORY", width=106)

    with connection() as db:
        rows = db.execute(
            """
            SELECT
                m.movement_id,
                p.sku,
                p.name,
                m.movement_type,
                m.quantity_change,
                m.previous_quantity,
                m.new_quantity,
                m.movement_at
            FROM stock_movements AS m
            JOIN products AS p
              ON p.product_id = m.product_id
            ORDER BY m.movement_id DESC
            """
        ).fetchall()

    if not rows:
        print("\nNo stock movements found.")
        return

    print(
        f"\n{'ID':<6}"
        f"{'SKU':<13}"
        f"{'Product':<24}"
        f"{'Type':<13}"
        f"{'Change':>9}"
        f"{'Before':>9}"
        f"{'After':>9}"
        f"{'Date':>21}"
    )
    print("-" * 104)

    for row in rows:
        print(
            f"{int(row['movement_id']):<6}"
            f"{shorten(str(row['sku']), 11):<13}"
            f"{shorten(str(row['name']), 22):<24}"
            f"{str(row['movement_type']):<13}"
            f"{int(row['quantity_change']):>+9}"
            f"{int(row['previous_quantity']):>9}"
            f"{int(row['new_quantity']):>9}"
            f"{format_datetime(str(row['movement_at'])):>21}"
        )

    print("-" * 104)


def export_products() -> None:
    """Export product inventory to CSV."""

    heading("EXPORT PRODUCTS")
    products = all_products()

    if not products:
        print("\nNo products are available to export.")
        return

    filename = EXPORT_DIR / (
        f"products_{datetime.now():%Y%m%d_%H%M%S}.csv"
    )

    try:
        with filename.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Product ID",
                    "SKU",
                    "Name",
                    "Category",
                    "Unit Price",
                    "Quantity",
                    "Reorder Level",
                    "Supplier",
                    "Created At",
                    "Updated At",
                ]
            )

            for product in products:
                writer.writerow(
                    [
                        product.product_id,
                        product.sku,
                        product.name,
                        product.category,
                        product.unit_price,
                        product.quantity,
                        product.reorder_level,
                        product.supplier,
                        product.created_at,
                        product.updated_at,
                    ]
                )
    except OSError as error:
        print(f"\nUnable to export products: {error}")
        return

    print(f"\nProducts exported successfully:\n{filename}")


def export_sales() -> None:
    """Export sales history to CSV."""

    heading("EXPORT SALES")

    with connection() as db:
        rows = db.execute(
            """
            SELECT
                s.sale_id,
                p.product_id,
                p.sku,
                p.name,
                s.quantity_sold,
                s.unit_price,
                s.total_amount,
                s.sold_at
            FROM sales AS s
            JOIN products AS p
              ON p.product_id = s.product_id
            ORDER BY s.sale_id
            """
        ).fetchall()

    if not rows:
        print("\nNo sales are available to export.")
        return

    filename = EXPORT_DIR / f"sales_{datetime.now():%Y%m%d_%H%M%S}.csv"

    try:
        with filename.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Sale ID",
                    "Product ID",
                    "SKU",
                    "Product",
                    "Quantity Sold",
                    "Unit Price",
                    "Total Amount",
                    "Sold At",
                ]
            )

            for row in rows:
                writer.writerow(
                    [
                        row["sale_id"],
                        row["product_id"],
                        row["sku"],
                        row["name"],
                        row["quantity_sold"],
                        row["unit_price"],
                        row["total_amount"],
                        row["sold_at"],
                    ]
                )
    except OSError as error:
        print(f"\nUnable to export sales: {error}")
        return

    print(f"\nSales exported successfully:\n{filename}")


def reports_menu() -> None:
    """Display reporting and export options."""

    while True:
        heading("REPORTS AND EXPORTS")
        print("1. Inventory summary")
        print("2. Low-stock report")
        print("3. Category report")
        print("4. Top-selling products")
        print("5. Stock movement history")
        print("6. Export products to CSV")
        print("7. Export sales to CSV")
        print("8. Back to main menu")

        choice = input("\nChoose an option from 1 to 8: ").strip()

        if choice == "1":
            inventory_summary()
        elif choice == "2":
            low_stock_report()
        elif choice == "3":
            category_report()
        elif choice == "4":
            top_selling_report()
        elif choice == "5":
            movement_history()
        elif choice == "6":
            export_products()
        elif choice == "7":
            export_sales()
        elif choice == "8":
            return
        else:
            print("\nInvalid option. Choose a number from 1 to 8.")

        pause()


def main() -> None:
    """Run the Inventory Management System."""

    initialize_database()

    while True:
        heading(APP_NAME)
        print("1. Product management")
        print("2. Stock and sales")
        print("3. Reports and CSV exports")
        print("4. Exit")

        choice = input("\nChoose an option from 1 to 4: ").strip()

        if choice == "1":
            product_menu()
        elif choice == "2":
            stock_sales_menu()
        elif choice == "3":
            reports_menu()
        elif choice == "4":
            print("\nThank you for using the Inventory Management System.")
            break
        else:
            print("\nInvalid option. Choose a number from 1 to 4.")
            pause()


if __name__ == "__main__":
    main()
