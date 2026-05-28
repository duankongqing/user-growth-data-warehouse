CREATE TABLE IF NOT EXISTS ods_users (
    user_id VARCHAR(50),
    register_time DATETIME,
    channel VARCHAR(50),
    device_type VARCHAR(20),
    gender VARCHAR(10),
    city VARCHAR(50),
    user_level VARCHAR(20),
    is_new_user INT,

    etl_time DATETIME,
    source_file VARCHAR(100)
);