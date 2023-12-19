INSERT INTO eperfume.Category (category_name) VALUES
('Floral'),
('Woody'),
('Citrus'),
('Oriental'),
('Fruity'),
('Aquatic'),
('Spicy'),
('Green'),
('Gourmand'),
('Chypre');

-- Sample data for Customer table
INSERT INTO eperfume.Customer (first_name, last_name, email, password, phone_number, address) VALUES
('John', 'Doe', 'john.doe@example.com', 'password123', '1234567890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', 'securepass', '9876543210', '456 Oak Ave'),
('Mike', 'Johnson', 'mike.johnson@example.com', 'pass123', '1112233445', '789 Pine Rd'),
('Sarah', 'Williams', 'sarah.williams@example.com', 'userpass', '5556667777', '101 Cedar Ln'),
('David', 'Brown', 'david.brown@example.com', 'mypassword', '8889990000', '202 Maple Dr'),
('Emily', 'Taylor', 'emily.taylor@example.com', 'letmein', '3334445555', '303 Birch Blvd'),
('Chris', 'Miller', 'chris.miller@example.com', 'access123', '4445556666', '404 Elm St'),
('Laura', 'Anderson', 'laura.anderson@example.com', 'password1', '7778889999', '505 Pine Ave'),
('Mark', 'Davis', 'mark.davis@example.com', 'secure123', '2223334444', '606 Oak Rd'),
('Rachel', 'Moore', 'rachel.moore@example.com', '1234pass', '9990001111', '707 Cedar Blvd');

-- Sample data for Products table
INSERT INTO eperfume.Products (product_name, category_id, price, stock_quantity) VALUES
('Rose Elegance', 1, 49.99, 100),
('Sandalwood Serenity', 2, 39.99, 80),
('Citrus Splash', 3, 29.99, 120),
('Oriental Nights', 4, 59.99, 60),
('Fruit Fusion', 5, 34.99, 90),
('Aqua Breeze', 6, 44.99, 70),
('Spice Sensation', 7, 54.99, 50),
('Green Meadows', 8, 49.99, 110),
('Gourmand Delight', 9, 64.99, 40),
('Chypre Essence', 10, 74.99, 30);

-- Sample data for Order table
INSERT INTO eperfume.Orders (customer_id, order_date, status, total_amount) VALUES
(1, '2023-01-15', 'Shipped', 149.97),
(2, '2023-02-20', 'Delivered', 119.98),
(3, '2023-03-25', 'Processing', 89.97),
(4, '2023-04-10', 'Shipped', 179.96),
(5, '2023-05-05', 'Delivered', 104.97),
(6, '2023-06-12', 'Processing', 134.98),
(7, '2023-07-18', 'Shipped', 164.97),
(8, '2023-08-23', 'Delivered', 129.98),
(9, '2023-09-30', 'Processing', 194.97),
(10, '2023-10-08', 'Shipped', 224.98);

-- Sample data for Order_Item table
INSERT INTO eperfume.Order_Item (order_id, product_id, quantity, price) VALUES
(1, 1, 2, 99.98),
(1, 3, 1, 29.99),
(2, 2, 3, 119.97),
(3, 5, 2, 69.98),
(4, 4, 1, 59.99),
(5, 6, 4, 179.96),
(6, 7, 1, 54.99),
(7, 8, 2, 99.98),
(8, 9, 3, 194.97),
(9, 10, 1, 74.99);

-- Sample data for Reviews table
INSERT INTO eperfume.Reviews (product_id, customer_id, rating, review_text, review_date) VALUES
(1, 1, 5, 'Amazing floral fragrance!', '2023-01-20'),
(2, 2, 4, 'Love the woody notes.', '2023-02-25'),
(3, 3, 3, 'Decent citrus scent.', '2023-03-30'),
(4, 4, 5, 'Exotic and oriental, my favorite!', '2023-04-15'),
(5, 5, 4, 'Nice fruity fragrance for daily wear.', '2023-05-10'),
(6, 6, 5, 'Refreshing aquatic scent!', '2023-06-17'),
(7, 7, 4, 'Spicy and intriguing.', '2023-07-23'),
(8, 8, 5, 'Green Meadows is a delightful scent.', '2023-08-28'),
(9, 9, 3, 'Gourmand Delight is too sweet for my taste.', '2023-10-05'),
(10, 10, 4, 'Chypre Essence has a unique charm.', '2023-10-12');

-- Sample data for Wishlist table
INSERT INTO eperfume.Wishlist (customer_id, product_id) VALUES
(1, 2),
(2, 4),
(3, 6),
(4, 8),
(5, 10),
(6, 1),
(7, 3),
(8, 5),
(9, 7),
(10, 9);

-- Sample data for Cart table
INSERT INTO eperfume.Cart (customer_id, product_id, quantity, price, total_price) VALUES
(1, 1, 2, 49.99, 99.98),
(2, 3, 1, 29.99, 29.99),
(3, 5, 2, 34.99, 69.98),
(4, 7, 1, 54.99, 54.99),
(5, 9, 3, 64.99, 194.97),
(6, 2, 2, 39.99, 79.98),
(7, 4, 1, 59.99, 59.99),
(8, 6, 4, 44.99, 179.96),
(9, 8, 2, 49.99, 99.98),
(10, 10, 1, 74.99, 74.99);

-- Sample data for Shipment table
INSERT INTO eperfume.Shipment (order_id, shipment_date, tracking_number, status) VALUES
(1, '2023-01-18', '123456789', 'Shipped'),
(2, '2023-02-22', '987654321', 'Delivered'),
(3, '2023-03-28', '555666777', 'Processing'),
(4, '2023-04-13', '111223344', 'Shipped'),
(5, '2023-05-08', '999000111', 'Delivered'),
(6, '2023-06-15', '333444555', 'Processing'),
(7, '2023-07-21', '444555666', 'Shipped'),
(8, '2023-08-26', '888999000', 'Delivered'),
(9, '2023-10-02', '222333444', 'Processing'),
(10, '2023-10-10', '777888999', 'Shipped');

-- Sample data for Payments table
INSERT INTO eperfume.Payments (order_id, payment_date, payment_method, amount) VALUES
(1, '2023-01-18', 'Credit Card', 149.97),
(2, '2023-02-22', 'PayPal', 119.98),
(3, '2023-03-28', 'Credit Card', 89.97),
(4, '2023-04-13', 'Debit Card', 179.96),
(5, '2023-05-08', 'PayPal', 104.97),
(6, '2023-06-15', 'Credit Card', 134.98),
(7, '2023-07-21', 'Debit Card', 164.97),
(8, '2023-08-26', 'PayPal', 129.98),
(9, '2023-10-02', 'Credit Card', 194.97),
(10, '2023-10-10', 'Debit Card', 224.98);

-- Sample data for Returns_Refunds table
INSERT INTO eperfume.Returns_Refunds (order_id, return_date, status, refund_amount) VALUES
(1, '2023-01-25', 'Refunded', 149.97),
(2, '2023-02-28', 'Processing', NULL),
(3, '2023-04-02', 'Processing', NULL),
(4, '2023-05-20', 'Refunded', 179.96),
(5, '2023-05-15', 'Refunded', 104.97),
(6, '2023-06-20', 'Processing', NULL),
(7, '2023-08-01', 'Refunded', 164.97),
(8, '2023-08-28', 'Processing', NULL),
(9, '2023-10-15', 'Processing', NULL),
(10, '2023-10-20', 'Refunded', 224.98);

-- Sample data for Promotions table
INSERT INTO eperfume.Promotions (promotion_name, start_date, end_date, discount_percent) VALUES
('Spring Sale', '2023-03-01', '2023-03-31', 15.00),
('Summer Special', '2023-06-01', '2023-08-31', 20.00),
('Back-to-School', '2023-09-01', '2023-09-30', 10.00),
('Holiday Joy', '2023-12-01', '2023-12-31', 25.00),
('Valentine\'s Day', '2023-02-01', '2023-02-14', 12.00),
('Mother\'s Day', '2023-05-01', '2023-05-15', 18.00),
('Black Friday', '2023-11-24', '2023-11-27', 30.00),
('Cyber Monday', '2023-11-27', '2023-11-30', 25.00),
('New Year Sale', '2023-12-31', '2024-01-01', 22.00),
('Mid-Year Clearance', '2023-07-01', '2023-07-15', 15.00);

