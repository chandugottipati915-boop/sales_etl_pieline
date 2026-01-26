-- Total revenue
SELECT SUM(quantity * price) AS total_revenue
FROM sales;

-- Monthly sales trend
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Top 5 customers
SELECT
    customer_name,
    SUM(quantity * price) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 5;