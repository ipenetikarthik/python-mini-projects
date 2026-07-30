# Inventory Management System

A professional command-line Inventory Management System developed using Python and SQLite.

The application helps businesses and individuals manage products, monitor stock quantities, record product sales, restock inventory, identify low-stock products, calculate inventory value, generate reports, and export business data to CSV files.

It uses an SQLite database for permanent storage and applies structured validation, database transactions, dataclasses, type hints, decimal-based currency calculations, and modular menu-driven programming.

---

## Features

### Product Management

- Add new products
- Generate automatic numeric product IDs
- Store a unique SKU for every product
- View all available products
- Search products by:
  - Product ID
  - SKU
  - Product name
  - Category
  - Supplier
- Update product details
- Update product prices
- Update reorder levels
- Update supplier information
- Adjust stock quantities manually
- Delete products that do not have sales history
- Prevent duplicate SKUs
- Validate all product inputs

### Stock Management

- Add opening stock while creating a product
- Restock existing products
- Adjust incorrect inventory quantities
- Automatically update stock after every sale
- Prevent stock quantities from becoming negative
- Record every inventory movement
- Maintain previous and updated stock quantities
- Store notes for stock adjustments
- Identify products that require restocking

### Sales Management

- Record product sales
- Select products by product ID or SKU
- Validate available stock before completing a sale
- Prevent sales above available quantity
- Calculate the total sale amount automatically
- Reduce inventory automatically after a sale
- Ask for confirmation before recording the sale
- Store complete sales history
- Display unit price, quantity sold, total amount and sale date

### Reports

- Display inventory summary
- Count total products
- Count total units in stock
- Calculate complete inventory value
- Count low-stock products
- Display total units sold
- Calculate total sales revenue
- Generate a low-stock report
- Generate a category-wise stock summary
- Rank top-selling products
- Display complete stock-movement history

### CSV Export

- Export complete product inventory to CSV
- Export complete sales history to CSV
- Generate timestamp-based export filenames
- Create export files automatically inside the `exports` folder
- Use UTF-8 encoding for Excel-compatible CSV files

### Data Storage

- Store application data using SQLite
- Create database tables automatically
- Maintain relationships between:
  - Products
  - Sales
  - Stock movements
- Enable foreign-key validation
- Create database indexes for faster searching
- Use database transactions for important stock operations

### Input Validation

- Validate required text fields
- Validate integers
- Validate decimal prices
- Validate minimum and maximum values
- Validate yes-or-no responses
- Validate product availability before sales
- Validate duplicate SKUs
- Validate stock corrections
- Validate deletion restrictions
- Handle SQLite errors safely

---

## Technologies Used

- Python 3
- SQLite
- Python `sqlite3` module
- Python `csv` module
- Python `decimal` module
- Python `datetime` module
- Python dataclasses
- Python type hints
- Python `pathlib` module
- Command-Line Interface
- Git
- GitHub

---

## Python Concepts Demonstrated

This project demonstrates:

- Variables
- Constants using `Final`
- Functions
- Dataclasses
- Frozen data structures
- Type hints
- Conditional statements
- Loops
- Lists
- Dictionaries
- Tuples
- String formatting
- Input validation
- Exception handling
- Decimal calculations
- File and directory handling
- CSV file handling
- Date and time handling
- SQLite database programming
- SQL CRUD operations
- SQL joins
- SQL aggregate functions
- SQL constraints
- Foreign-key relationships
- Database indexes
- Database transactions
- Search functionality
- Sorting
- Menu-driven programming
- Modular application design
- Main-program execution

```python
if __name__ == "__main__":
    main()
```

---

## Project Structure

```text
python-mini-projects/
│
└── 06-inventory-management-system/
    │
    ├── inventory_management.py
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    │
    ├── database/
    │   └── inventory.db
    │
    ├── exports/
    │   └── .gitkeep
    │
    └── screenshots/
        └── .gitkeep
```

The SQLite database is created automatically when the application runs for the first time.

Generated CSV reports are stored inside the `exports` folder.

---

## Database Design

The project uses three main SQLite tables.

### `products`

Stores product and inventory information.

Important columns:

```text
product_id
sku
name
category
unit_price
quantity
reorder_level
supplier
created_at
updated_at
```

### `sales`

Stores completed product sales.

Important columns:

```text
sale_id
product_id
quantity_sold
unit_price
total_amount
sold_at
```

### `stock_movements`

Stores every inventory change.

Important columns:

```text
movement_id
product_id
movement_type
quantity_change
previous_quantity
new_quantity
notes
movement_at
```

---

## Database Relationships

The application uses foreign-key relationships.

```text
products
   │
   ├── sales
   │
   └── stock_movements
```

Every sale is connected to a valid product.

Every stock movement is also connected to a valid product.

Foreign-key checking is enabled using:

```python
connection.execute("PRAGMA foreign_keys = ON")
```

---

## Installation

### 1. Install Python

Make sure Python 3.10 or later is installed.

Check the installed version:

```bash
python --version
```

On some systems:

```bash
python3 --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/ipenetikarthik/python-mini-projects.git
```

---

### 3. Open the Project Folder

```bash
cd python-mini-projects/06-inventory-management-system
```

---

### 4. Run the Application

```bash
python inventory_management.py
```

On some systems:

```bash
python3 inventory_management.py
```

On Windows, this command may also work:

```bash
py inventory_management.py
```

---

## Application Menu

After running the project, the main menu appears:

```text
======================================================================================
                         INVENTORY MANAGEMENT SYSTEM
======================================================================================
1. Product management
2. Stock and sales
3. Reports and CSV exports
4. Exit

Choose an option from 1 to 4:
```

---

## Product Management Menu

Select:

```text
1
```

The following menu appears:

```text
======================================================================================
                              PRODUCT MANAGEMENT
======================================================================================
1. Add product
2. View all products
3. Search products
4. Update product
5. Adjust stock
6. Delete product
7. Back to main menu
```

---

## Add a Product

Select:

```text
1
```

The program asks for:

- SKU
- Product name
- Category
- Unit price
- Opening quantity
- Reorder level
- Supplier name

Example:

```text
SKU: LAP001
Product name: Dell Latitude Laptop
Category: Electronics
Unit price: 45000
Opening quantity: 10
Reorder level [default 5]: 3
Supplier name: Dell Technologies
```

Possible result:

```text
Product added successfully with ID 1.
```

The application prevents another product from using the same SKU.

---

## View All Products

Select:

```text
2
```

Example output:

```text
ID    SKU          Product                 Category             Price    Qty      Status
--------------------------------------------------------------------------------------------
1     LAP001       Dell Latitude Laptop    Electronics     ₹45,000.00     10    In Stock
2     KEY001       Wireless Keyboard       Accessories      ₹1,200.00     20    In Stock
3     MOU001       Wireless Mouse          Accessories        ₹750.00      4   LOW STOCK
--------------------------------------------------------------------------------------------
Total records: 3
```

A product is marked as `LOW STOCK` when:

```text
quantity <= reorder level
```

---

## Search Products

Select:

```text
3
```

The user may search using:

- Product ID
- SKU
- Product name
- Category
- Supplier

Example:

```text
Enter ID, SKU, product, category or supplier: keyboard
```

The application uses SQL `LIKE` queries to return matching products.

---

## Update Product

Select:

```text
4
```

The application asks for either:

```text
Product ID
```

or:

```text
SKU
```

Users may update:

- SKU
- Product name
- Category
- Unit price
- Reorder level
- Supplier

Pressing Enter keeps the current value.

Example:

```text
SKU [KEY001]:
Product name [Wireless Keyboard]:
Category [Computer Accessories]:
Unit price [1200.00]: 1350
Reorder level [5]:
Supplier [Logitech]:
```

---

## Adjust Stock

Select:

```text
5
```

This option is useful when the physical inventory does not match the system quantity.

Example:

```text
Enter product ID or SKU: MOU001
Current quantity for Wireless Mouse: 4
Enter corrected quantity: 6
Reason for adjustment: Two units were not previously recorded
```

The application records:

- Previous quantity
- New quantity
- Difference
- Reason
- Date and time

---

## Delete Product

Select:

```text
6
```

A product may be deleted only when it does not have sales history.

The application asks for confirmation:

```text
Delete this product? (y/N):
```

Products with completed sales cannot be deleted because removing them would damage historical sales records.

---

## Stock and Sales Menu

From the main menu, select:

```text
2
```

The following menu appears:

```text
======================================================================================
                                STOCK AND SALES
======================================================================================
1. Restock product
2. Record sale
3. View sales history
4. Back to main menu
```

---

## Restock Product

Select:

```text
1
```

Example:

```text
Enter product ID or SKU: KEY001
Product         : Wireless Keyboard
Current quantity: 20
Quantity to add: 10
Restock note [optional]: New supplier delivery
```

Possible output:

```text
Product restocked successfully.
New quantity: 30
```

The restock operation is also recorded in the stock-movement table.

---

## Record a Sale

Select:

```text
2
```

Example:

```text
Enter product ID or SKU: KEY001

Product       : Wireless Keyboard
Available     : 30
Unit price    : ₹1,350.00

Quantity sold: 2
Total amount  : ₹2,700.00
Confirm this sale? (Y/n): y
```

Possible output:

```text
Sale recorded successfully.
Remaining stock: 28
```

The application automatically:

1. Validates available stock.
2. Calculates the total amount.
3. Saves the sale.
4. Reduces product quantity.
5. Records the stock movement.
6. Commits all changes as one database transaction.

---

## Sales History

Select:

```text
3
```

Example output:

```text
Sale ID  SKU          Product                    Qty     Unit Price          Total               Sold At
---------------------------------------------------------------------------------------------------------
1        KEY001       Wireless Keyboard            2      ₹1,350.00      ₹2,700.00   31-07-2026 12:30 AM
---------------------------------------------------------------------------------------------------------
Total records: 1
```

---

## Reports and CSV Exports

From the main menu, select:

```text
3
```

The following menu appears:

```text
======================================================================================
                             REPORTS AND EXPORTS
======================================================================================
1. Inventory summary
2. Low-stock report
3. Category summary
4. Top-selling products
5. Stock movement history
6. Export products to CSV
7. Export sales to CSV
8. Back to main menu
```

---

## Inventory Summary

This report displays:

- Number of products
- Total units in stock
- Number of low-stock products
- Total inventory value
- Total units sold
- Total sales revenue

Example:

```text
Number of products                                      3
Total units in stock                                   42
Low-stock products                                      1
Inventory value                               ₹483,000.00
Total units sold                                        2
Total sales revenue                             ₹2,700.00
```

---

## Inventory Value Calculation

Inventory value is calculated using:

```text
unit price × available quantity
```

Example:

```text
₹45,000 × 10 = ₹450,000
```

The application uses `Decimal` rather than floating-point arithmetic for reliable currency calculations.

---

## Low-Stock Report

The low-stock report shows products where:

```text
quantity <= reorder level
```

Example:

```text
ID    SKU          Product                   Supplier                 Qty   Reorder
-------------------------------------------------------------------------------------
3     MOU001       Wireless Mouse            HP                         4         5
-------------------------------------------------------------------------------------
Products requiring attention: 1
```

---

## Category Summary

The category report groups inventory by product category.

It displays:

- Category name
- Number of products
- Total units
- Total stock value

Example:

```text
Category                        Products       Units         Stock Value
------------------------------------------------------------------------
Computer Accessories                  2          32          ₹52,800.00
Electronics                           1          10         ₹450,000.00
------------------------------------------------------------------------
```

---

## Top-Selling Products

The project ranks products using total quantity sold.

Example:

```text
Rank    SKU           Product                         Units Sold           Revenue
--------------------------------------------------------------------------------------
1       KEY001        Wireless Keyboard                        2         ₹2,700.00
--------------------------------------------------------------------------------------
```

The ranking uses SQL aggregate functions:

```sql
SUM(quantity_sold)
```

and:

```sql
SUM(total_amount)
```

---

## Stock Movement History

Every inventory change is recorded.

Supported movement types include:

```text
INITIAL
RESTOCK
SALE
ADJUSTMENT
```

Example:

```text
ID    SKU          Product                Type          Change   Before   After                 Date
-------------------------------------------------------------------------------------------------------
3     KEY001       Wireless Keyboard      SALE              -2       30      28   31-07-2026 12:30 AM
2     KEY001       Wireless Keyboard      RESTOCK          +10       20      30   31-07-2026 12:25 AM
1     KEY001       Wireless Keyboard      INITIAL          +20        0      20   31-07-2026 12:20 AM
-------------------------------------------------------------------------------------------------------
```

This creates a clear inventory audit trail.

---

## Product CSV Export

Select:

```text
6
```

The project creates a file such as:

```text
exports/products_20260731_003500.csv
```

The exported file contains:

```text
Product ID
SKU
Name
Category
Unit Price
Quantity
Reorder Level
Supplier
Created At
Updated At
```

---

## Sales CSV Export

Select:

```text
7
```

The project creates a file such as:

```text
exports/sales_20260731_003700.csv
```

The exported file contains:

```text
Sale ID
Product ID
SKU
Product Name
Quantity Sold
Unit Price
Total Amount
Sold At
```

---

## Currency Handling

The application uses Python's `Decimal` class.

```python
from decimal import Decimal
```

Currency values are rounded to two decimal places using:

```python
Decimal("0.01")
```

This is more reliable than using floating-point numbers for financial calculations.

---

## Input Validation

The application validates:

- Empty product names
- Empty categories
- Empty supplier names
- Empty SKUs
- Duplicate SKUs
- Invalid whole numbers
- Negative stock quantities
- Invalid decimal prices
- Prices below the accepted minimum
- Invalid menu selections
- Invalid yes-or-no responses
- Sales above available stock
- Missing products
- Deletion of products with sales history
- Stock adjustments without reasons

Users are repeatedly prompted until valid input is provided.

---

## Database Transactions

Important operations use SQLite transactions.

For example, recording a sale requires:

1. Inserting a sales record.
2. Reducing inventory quantity.
3. Recording a stock movement.

These actions are executed together inside one database connection.

This prevents partially completed inventory operations.

---

## Main Dataclasses

### `Product`

Stores product information.

```python
@dataclass(frozen=True, slots=True)
class Product:
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
```

### `Sale`

Stores sales information.

```python
@dataclass(frozen=True, slots=True)
class Sale:
    sale_id: int
    product_id: int
    sku: str
    product_name: str
    quantity_sold: int
    unit_price: Decimal
    total_amount: Decimal
    sold_at: str
```

Frozen dataclasses help prevent accidental modification after records are loaded.

---

## Main Functions

### `initialize_database()`

Creates the required database tables and indexes.

### `create_connection()`

Creates and configures a SQLite connection.

### `add_product()`

Collects product information and inserts a new product.

### `view_all_products()`

Displays all products.

### `search_products()`

Searches inventory using multiple fields.

### `update_product()`

Updates product details.

### `adjust_stock()`

Corrects inventory quantity and records the change.

### `delete_product()`

Deletes eligible products.

### `restock_product()`

Adds inventory and creates a restock movement.

### `record_sale()`

Records a sale, reduces stock and creates a movement record.

### `view_sales_history()`

Displays complete sales history.

### `inventory_summary()`

Displays key inventory and sales totals.

### `low_stock_report()`

Displays products at or below reorder level.

### `category_summary()`

Groups products by category.

### `top_selling_products()`

Ranks products based on sales.

### `stock_movement_history()`

Displays complete inventory activity.

### `export_products_csv()`

Exports inventory records.

### `export_sales_csv()`

Exports sales records.

### `main()`

Controls the complete application workflow.

---

## Suggested Sample Products

### Product 1

```text
SKU: LAP001
Product name: Dell Latitude Laptop
Category: Electronics
Unit price: 45000
Opening quantity: 10
Reorder level: 3
Supplier name: Dell Technologies
```

### Product 2

```text
SKU: KEY001
Product name: Wireless Keyboard
Category: Computer Accessories
Unit price: 1200
Opening quantity: 20
Reorder level: 5
Supplier name: Logitech
```

### Product 3

```text
SKU: MOU001
Product name: Wireless Mouse
Category: Computer Accessories
Unit price: 750
Opening quantity: 4
Reorder level: 5
Supplier name: HP
```

---

## Recommended Testing Flow

1. Add three or more products.
2. View the product list.
3. Search for a product using its SKU.
4. Update the product price.
5. Restock one product.
6. Record at least one sale.
7. Check the remaining stock.
8. Open the inventory summary.
9. Open the low-stock report.
10. Open the category summary.
11. Open the top-selling-products report.
12. View stock movement history.
13. Export products to CSV.
14. Export sales to CSV.
15. Verify the generated files inside the `exports` folder.

---

## Screenshots

Recommended screenshot filenames:

```text
screenshots/
├── 01-main-menu.png
├── 02-add-product.png
├── 03-product-list.png
├── 04-search-product.png
├── 05-restock-product.png
├── 06-record-sale.png
├── 07-sales-history.png
├── 08-inventory-summary.png
├── 09-low-stock-report.png
├── 10-category-summary.png
├── 11-top-selling-products.png
└── 12-stock-movement-history.png
```

Add screenshots to this section after uploading them:

```markdown
## Application Screenshots

### Main Menu

![Main Menu](screenshots/01-main-menu.png)

### Product List

![Product List](screenshots/03-product-list.png)

### Record Sale

![Record Sale](screenshots/06-record-sale.png)

### Inventory Summary

![Inventory Summary](screenshots/08-inventory-summary.png)

### Low-Stock Report

![Low-Stock Report](screenshots/09-low-stock-report.png)
```

---

## Git Commit Messages

Initial project commit:

```bash
git commit -m "Build Mini Project 06 inventory management system with Python and SQLite"
```

After adding screenshots:

```bash
git commit -m "Add inventory management system screenshots"
```

After improving documentation:

```bash
git commit -m "Improve Project 06 README and usage documentation"
```

After fixing validation:

```bash
git commit -m "Fix product validation and inventory transaction handling"
```

---

## Learning Outcomes

By developing this project, I practised:

- Designing a complete command-line application
- Working with SQLite databases
- Creating relational database tables
- Applying foreign-key relationships
- Performing SQL CRUD operations
- Writing SQL joins
- Using SQL aggregate functions
- Managing database transactions
- Preventing duplicate records
- Tracking inventory changes
- Recording product sales
- Calculating revenue
- Calculating inventory value
- Creating low-stock warnings
- Working with Python dataclasses
- Applying strict type annotations
- Using `Decimal` for currency values
- Validating user input
- Handling database exceptions
- Exporting application data to CSV
- Managing files and directories
- Creating professional project documentation
- Managing source code using Git and GitHub

---

## Future Enhancements

Future versions may include:

- Product barcode support
- QR-code support
- Supplier-management module
- Customer-management module
- Purchase-order management
- Sales invoices
- PDF invoice generation
- GST calculation
- Product-return management
- Expiry-date tracking
- Batch-number tracking
- Multiple warehouse support
- User login and role-based access
- Admin and employee accounts
- Daily, monthly and yearly sales reports
- Date-range filtering
- Sales charts
- Inventory charts
- Excel export
- Email low-stock notifications
- Automated backups
- Unit tests
- Logging
- REST API using FastAPI
- Web application using Django
- Desktop interface using Tkinter
- Frontend dashboard using React

---

## Repository

The complete source code is available in:

[Python Mini Projects](https://github.com/ipenetikarthik/python-mini-projects)

---

## Author

### Peneti Karthik

Python Developer focused on practical application development, backend fundamentals, databases, APIs, automation and continuous learning.

- **GitHub:** [github.com/ipenetikarthik](https://github.com/ipenetikarthik)
- **LinkedIn:** [linkedin.com/in/ipenetikarthik](https://www.linkedin.com/in/ipenetikarthik)
- **Blog:** [ipenetikarthik.blogpage.com](https://ipenetikarthik.blogpage.com)
- **ORCID:** [0009-0004-6000-6129](https://orcid.org/0009-0004-6000-6129)

---

## License

This project is part of the `python-mini-projects` repository and is licensed under the [MIT License](../LICENSE).

---

<p align="center">
  <strong>Thank you for visiting the Inventory Management System project.</strong>
</p>

<p align="center">
  Developed by Peneti Karthik
</p>
