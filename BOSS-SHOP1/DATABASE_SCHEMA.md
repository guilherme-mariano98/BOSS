# Boss Shop - Database Schema Documentation

This document describes the database schema for the Boss Shop application, which uses SQLite as its database engine.

## Database Engine
- **Engine**: SQLite
- **Database File**: `db.sqlite3`

## Tables

### 1. Users
Stores user account information and profile data.

**Fields:**
- `id` (BigAutoField) - Primary key
- `password` (CharField) - Hashed password
- `last_login` (DateTimeField) - Last login timestamp
- `is_superuser` (BooleanField) - Superuser status
- `username` (CharField) - Unique username
- `first_name` (CharField) - User's first name
- `last_name` (CharField) - User's last name
- `email` (EmailField) - Unique email address
- `is_staff` (BooleanField) - Staff status
- `is_active` (BooleanField) - Active status
- `date_joined` (DateTimeField) - Account creation timestamp
- `created_at` (DateTimeField) - Profile creation timestamp
- `phone` (CharField) - Phone number (nullable)
- `birth_date` (DateField) - Birth date (nullable)
- `gender` (CharField) - Gender (nullable)
- `cpf` (CharField) - Brazilian CPF (nullable)

**Relationships:**
- One-to-Many with Addresses (user -> addresses)
- One-to-Many with PaymentMethods (user -> payment_methods)
- One-to-One with NotificationPreference (user -> notification_preference)

### 2. Addresses
Stores user address information.

**Fields:**
- `id` (BigAutoField) - Primary key
- `name` (CharField) - Address label (e.g., "Home", "Work")
- `street` (CharField) - Street address
- `city` (CharField) - City
- `state` (CharField) - State abbreviation (Brazilian states)
- `zip_code` (CharField) - ZIP code
- `country` (CharField) - Country (default: "Brasil")
- `is_default` (BooleanField) - Default address flag
- `created_at` (DateTimeField) - Creation timestamp
- `user_id` (ForeignKey) - Reference to User

### 3. PaymentMethods
Stores user payment method information.

**Fields:**
- `id` (BigAutoField) - Primary key
- `type` (CharField) - Payment type with choices:
  - `credit_card` - Credit Card
  - `debit_card` - Debit Card
  - `pix` - PIX
  - `boleto` - Boleto
- `name` (CharField) - Payment method name (e.g., "Visa ****1234")
- `is_default` (BooleanField) - Default payment method flag
- `created_at` (DateTimeField) - Creation timestamp
- `user_id` (ForeignKey) - Reference to User

### 4. NotificationPreferences
Stores user notification preferences.

**Fields:**
- `id` (BigAutoField) - Primary key
- `promotions` (BooleanField) - Receive promotional notifications (default: True)
- `order_status` (BooleanField) - Receive order status updates (default: True)
- `new_products` (BooleanField) - Receive new product notifications (default: False)
- `newsletter` (BooleanField) - Receive newsletter (default: False)
- `updated_at` (DateTimeField) - Last update timestamp
- `user_id` (OneToOneField) - Reference to User

### 5. Categories
Stores product categories.

**Fields:**
- `id` (BigAutoField) - Primary key
- `name` (CharField) - Category name
- `slug` (SlugField) - URL-friendly category identifier
- `description` (TextField) - Category description
- `created_at` (DateTimeField) - Creation timestamp

### 6. Products
Stores product information.

**Fields:**
- `id` (BigAutoField) - Primary key
- `name` (CharField) - Product name
- `description` (TextField) - Product description
- `price` (DecimalField) - Product price
- `image` (ImageField) - Product image (nullable)
- `created_at` (DateTimeField) - Creation timestamp
- `updated_at` (DateTimeField) - Last update timestamp
- `category_id` (ForeignKey) - Reference to Category

### 7. Orders
Stores order information.

**Fields:**
- `id` (BigAutoField) - Primary key
- `total_amount` (DecimalField) - Order total
- `status` (CharField) - Order status with choices:
  - `pending` - Pending
  - `processing` - Processing
  - `shipped` - Shipped
  - `delivered` - Delivered
  - `cancelled` - Cancelled
- `shipping_address` (TextField) - Shipping address
- `payment_method` (CharField) - Payment method used
- `created_at` (DateTimeField) - Creation timestamp
- `updated_at` (DateTimeField) - Last update timestamp
- `user_id` (ForeignKey) - Reference to User

### 8. OrderItems
Stores individual items within an order.

**Fields:**
- `id` (BigAutoField) - Primary key
- `quantity` (PositiveIntegerField) - Item quantity
- `price` (DecimalField) - Item price
- `order_id` (ForeignKey) - Reference to Order
- `product_id` (ForeignKey) - Reference to Product

## Relationships Summary

```
Users 1 ---< Addresses
Users 1 ---< PaymentMethods
Users 1 ---- NotificationPreferences
Categories 1 ---< Products
Products 1 ---< OrderItems >--- Orders
Users 1 ---< Orders
```

## Migration History

The database schema is managed through Django migrations. Key migrations include:

1. `0001_initial` - Initial migration with basic models (Category, Product, Order, OrderItem, User)
2. `0002_auto_20251013_1915` - Added profile fields to User model and created Address, PaymentMethod, and NotificationPreference models

## Notes

- All foreign key relationships use CASCADE deletion, meaning when a parent record is deleted, all related child records are also deleted.
- The User model extends Django's AbstractUser to provide custom fields while maintaining all built-in authentication functionality.
- Timestamps are automatically managed with `auto_now` and `auto_now_add` attributes.
- The database is designed to support Brazilian-specific features like CPF and state abbreviations.