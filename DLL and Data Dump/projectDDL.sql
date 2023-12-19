-- Promotions table
CREATE TABLE eperfume.Promotions (
    promotion_id INT PRIMARY KEY AUTO_INCREMENT,
    promotion_name VARCHAR(255),
    start_date DATE,
    end_date DATE,
    discount_percent DECIMAL(5,2) CHECK (discount_percent >= 0.0 AND discount_percent <= 100.0)
);

-- Customer table
CREATE TABLE eperfume.Customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) UNIQUE,
    phone_number VARCHAR(20),
    address VARCHAR(255)
);

-- Category table
CREATE TABLE eperfume.Category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(255)
);

-- Products table
CREATE TABLE eperfume.Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255),
    category_id INT,
    price DECIMAL(10, 2),
    stock_quantity INT,
    FOREIGN KEY (category_id) REFERENCES eperfume.Category(category_id) ON DELETE SET NULL
);

-- Order table
CREATE TABLE eperfume.Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    status VARCHAR(50),
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES eperfume.Customer(customer_id) ON DELETE SET NULL
);

-- Returns_Refunds table
CREATE TABLE eperfume.Returns_Refunds (
    return_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    return_date DATE,
    status VARCHAR(50),
    refund_amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES eperfume.Orders(order_id) ON DELETE CASCADE
);

-- Shipment table
CREATE TABLE eperfume.Shipment (
    shipment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    shipment_date DATE,
    tracking_number VARCHAR(50),
    status VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES eperfume.Orders(order_id) ON DELETE CASCADE
);

CREATE TABLE eperfume.Payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    payment_date DATE,
    payment_method VARCHAR(50),
    amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES eperfume.Orders(order_id) ON DELETE CASCADE
);


-- Order_Item table
CREATE TABLE eperfume.Order_Item (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT CHECK (quantity > 0),
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES eperfume.Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES eperfume.Products(product_id) ON DELETE SET NULL
);

-- Reviews table
CREATE TABLE eperfume.Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    customer_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES eperfume.Products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES eperfume.Customer(customer_id) ON DELETE SET NULL
);

-- Cart table
CREATE TABLE eperfume.Cart (
    cart_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT CHECK (quantity > 0),
    price DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES eperfume.Customer(customer_id) ON DELETE SET NULL,
    FOREIGN KEY (product_id) REFERENCES eperfume.Products(product_id) ON DELETE CASCADE
);

-- Wishlist table
CREATE TABLE eperfume.Wishlist (
    wishlist_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES eperfume.Customer(customer_id) ON DELETE SET NULL,
    FOREIGN KEY (product_id) REFERENCES eperfume.Products(product_id) ON DELETE CASCADE
);


