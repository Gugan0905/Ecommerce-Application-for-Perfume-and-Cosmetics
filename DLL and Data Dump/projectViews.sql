/* Customer Order Summary View */

CREATE VIEW CustomerOrderSummary AS
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent,
    AVG(o.total_amount) AS avg_order_value
FROM 
    eperfume.Customer c
JOIN 
    eperfume.Orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, customer_name;

/* Product Sales and Reviews View */

CREATE VIEW ProductSalesReviews AS
SELECT 
    p.product_id,
    p.product_name,
    COUNT(oi.order_item_id) AS total_sales_quantity,
    SUM(oi.quantity * oi.price) AS total_sales_revenue,
    AVG(r.rating) AS avg_rating
FROM 
    eperfume.Products p
LEFT JOIN 
    eperfume.Order_Item oi ON p.product_id = oi.product_id
LEFT JOIN 
    eperfume.Reviews r ON p.product_id = r.product_id
GROUP BY 
    p.product_id, p.product_name;