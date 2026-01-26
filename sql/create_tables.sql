CREATE TABLE IF NOT EXISTS sales (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(10),
    product VARCHAR(100),
    quantity INT,
    price NUMERIC(10,2),
    order_date DATE,
    region VARCHAR(20),
    total_amount NUMERIC(10,2)
);

CREATE INDEX idx_order_date ON sales(order_date);
CREATE INDEX idx_customer_id ON sales(customer_id);



CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name TEXT,
    price NUMERIC(10,2),
    category TEXT
);