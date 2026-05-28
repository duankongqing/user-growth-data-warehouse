DROP TABLE IF EXISTS dws_user_trade_1d;

CREATE TABLE dws_user_trade_1d AS

SELECT

    dt,

    user_id,

    COUNT(DISTINCT user_id) AS order_user_cnt,

    COUNT(order_id) AS order_cnt,

    SUM(
        CASE
            WHEN pay_status = '已支付'
            THEN 1
            ELSE 0
        END
    ) AS paid_order_cnt,

    SUM(
        CASE
            WHEN pay_status = '已支付'
            THEN order_amount
            ELSE 0
        END
    ) AS paid_gmv,

    AVG(
        CASE
            WHEN pay_status = '已支付'
            THEN order_amount
            ELSE NULL
        END
    ) AS avg_paid_order_amount

FROM dwd_fact_order_info

GROUP BY dt,user_id;