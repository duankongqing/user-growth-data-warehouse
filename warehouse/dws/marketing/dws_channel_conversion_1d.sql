DROP TABLE IF EXISTS dws_channel_conversion_1d;

CREATE TABLE dws_channel_conversion_1d AS

SELECT

    order_channel,

    COUNT(DISTINCT user_id) AS user_cnt,

    COUNT(order_id) AS order_cnt,

    SUM(order_amount) AS total_gmv

FROM dwd_fact_order_info

GROUP BY order_channel;