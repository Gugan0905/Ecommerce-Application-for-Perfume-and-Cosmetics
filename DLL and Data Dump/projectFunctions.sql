/* Function to Calculate Total Sales for a Product: */
SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER $$

DROP FUNCTION IF EXISTS total_sales $$
CREATE FUNCTION total_sales(prodid INT) 
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE total DECIMAL(10, 2);
    SELECT SUM(price * quantity) INTO total
    FROM eperfume.Order_Item
    WHERE product_id = prodid;
    RETURN total;
END $$

DELIMITER ;

/* Function to Check Stock Availability: */

DELIMITER $$

DROP FUNCTION IF EXISTS is_in_stock $$ 
CREATE FUNCTION is_in_stock(prodid INT) 
RETURNS BOOLEAN
BEGIN
    DECLARE stock_count INT DEFAULT 0;
    SELECT SUM(stock_quantity) INTO stock_count
    FROM eperfume.Products
    WHERE product_id = prodid
    GROUP BY product_id;
 
    RETURN stock_count > 0;
END $$
 
DELIMITER ;

/* Function to Calculate Refund Amount for an Order: */

DELIMITER $$

DROP FUNCTION IF EXISTS calculate_refund $$ 
CREATE FUNCTION calculate_refund(ordid INT) 
RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE refund DECIMAL(10, 2);
    SELECT SUM(price) INTO refund
    FROM eperfume.Order_Item
    WHERE order_id = ordid;
    RETURN refund;
END $$

DELIMITER ;