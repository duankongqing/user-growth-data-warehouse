CREATE TABLE IF NOT EXISTS ods_events (
    event_id VARCHAR(50),

    user_id VARCHAR(50),
    event_time DATETIME,
    event_type VARCHAR(50),
    page_name VARCHAR(50),
    device_type VARCHAR(20),
    stay_duration INT,

    etl_time DATETIME,
    source_file VARCHAR(100)
);