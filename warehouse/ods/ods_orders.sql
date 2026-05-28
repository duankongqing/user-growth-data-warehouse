CREATE TABLE IF NOT EXISTS ods_orders (
    order_id VARCHAR(50),
    user_id VARCHAR(50),
    order_time DATETIME,
    order_amount DECIMAL(10,2),
    pay_status VARCHAR(20),
    goods_num INT,
    pay_method VARCHAR(20),
    order_channel VARCHAR(50),

    etl_time DATETIME,
    source_file VARCHAR(100)
);