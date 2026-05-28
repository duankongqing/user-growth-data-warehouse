DROP TABLE IF EXISTS dwd_dim_user_info;

CREATE TABLE dwd_dim_user_info AS

SELECT

    user_id,
    register_time,
    channel,
    device_type,
    gender,
    city,

    CASE
        WHEN user_level IS NULL
        THEN '普通用户'
        ELSE user_level
    END AS user_level,

    is_new_user,

    DATE(register_time) AS dt

FROM ods_users;