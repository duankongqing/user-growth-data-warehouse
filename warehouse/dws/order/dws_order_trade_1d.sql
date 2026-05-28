DROP TABLE IF EXISTS dws_order_trade_1d;

CREATE TABLE dws_order_trade_1d AS

SELECT

    dt,

    COUNT(order_id) AS order_cnt,

    SUM(order_amount) AS total_gmv,

    AVG(order_amount) AS avg_order_amount,

    MAX(order_amount) AS max_order_amount,

    MIN(order_amount) AS min_order_amount,

    COUNT(
        CASE WHEN pay_status = '已支付'
             THEN 1
        END
    ) as paid_order_cnt

FROM dwd_fact_order_info

GROUP BY dt;