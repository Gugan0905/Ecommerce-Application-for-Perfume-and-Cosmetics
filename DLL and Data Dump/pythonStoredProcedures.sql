DELIMITER //

DROP PROCEDURE IF EXISTS ReduceStockQuantity //
CREATE PROCEDURE ReduceStockQuantity(
    IN productId_arg INT,
    IN reduceAmount INT
)
BEGIN
    UPDATE Products
    SET stock_quantity = stock_quantity - reduceAmount
    WHERE product_id = productId_arg;
END //

DROP PROCEDURE IF EXISTS RefundOrder //
CREATE PROCEDURE RefundOrder(
    IN orderID INT
)
BEGIN
    UPDATE Orders
    SET status = 'Returned'
    WHERE order_id = orderID;
    
    INSERT INTO Returns_Refunds
    (order_id, return_date, status, refund_amount)
    VALUES
    (orderID, CURDATE(), 'Processing', NULL);
END //

DROP PROCEDURE IF EXISTS ProcessOrder//
CREATE PROCEDURE ProcessOrder (
    IN orderID INT,
    IN productIDs VARCHAR(255), -- Comma-separated product IDs
    IN quantities VARCHAR(255), -- Comma-separated quantities
    IN prices VARCHAR(255), -- Comma-separated prices
    IN payment_method_str VARCHAR(50),
    IN current_customer_id INT
)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE product_id INT;
    DECLARE quantity INT;
    DECLARE price DECIMAL(10, 2);

    WHILE i <= LENGTH(productIDs) - LENGTH(REPLACE(productIDs, ',', '')) + 1 DO
        SET product_id = SUBSTRING_INDEX(SUBSTRING_INDEX(productIDs, ',', i), ',', -1);
        SET quantity = SUBSTRING_INDEX(SUBSTRING_INDEX(quantities, ',', i), ',', -1);
        SET price = SUBSTRING_INDEX(SUBSTRING_INDEX(prices, ',', i), ',', -1);

        -- Insert into Order_Item
        INSERT INTO Order_Item (order_id, product_id, quantity, price)
        VALUES (orderID, product_id, quantity, price);

        SET i = i + 1;
    END WHILE;

    -- Insert into Payments
    INSERT INTO Payments (order_id, payment_date, payment_method)
    VALUES (orderID, CURDATE(), payment_method_str);

    -- Insert into Shipment
    INSERT INTO Shipment (order_id, shipment_date, tracking_number, status)
    VALUES (orderID, CURDATE(), 10101010101, 'Processing');

    -- Delete from Cart
    DELETE FROM Cart WHERE customer_id = current_customer_id;
END //

DELIMITER ;
