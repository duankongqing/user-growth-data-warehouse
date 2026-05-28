DROP TABLE IF EXISTS dwd_fact_order_info;

CREATE TABLE dwd_fact_order_info AS

SELECT
    order_id,
    user_id,
    order_time,
    order_amount,
    pay_status,
    goods_num,
    pay_method,
    order_channel,
    DATE(order_time) AS dt

FROM (

    SELECT
        order_id,
        user_id,
        order_time,
        order_amount,
        pay_status,
        goods_num,
        pay_method,
        order_channel,

        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY order_time DESC
        ) AS rn

    FROM ods_orders

    WHERE
        order_amount > 0
        AND goods_num > 0
        AND pay_status IN ('已支付', '未支付')

) t

WHERE rn = 1;