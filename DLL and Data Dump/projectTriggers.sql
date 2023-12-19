DELIMITER //
CREATE TRIGGER DeleteWishlist 
AFTER INSERT ON Cart 
FOR EACH ROW 
BEGIN
     -- Deleting from Wishlist table based on the product_id in the newly inserted row     
     DELETE FROM Wishlist WHERE product_id = NEW.product_id; 
END //

DELIMITER ;
