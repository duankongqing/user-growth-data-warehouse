DROP TABLE IF EXISTS dws_funnel_conversion_1d;

CREATE TABLE dws_funnel_conversion_1d AS

SELECT

    dt,

    home_cnt,

    product_cnt,

    cart_cnt,

    pay_cnt,

    ROUND(
        product_cnt / NULLIF(home_cnt, 0),
        2
    ) AS home_to_product_rate,

    ROUND(
        cart_cnt / NULLIF(product_cnt, 0),
        2
    ) AS product_to_cart_rate,

    ROUND(
        pay_cnt / NULLIF(cart_cnt, 0),
        2
    ) AS cart_to_pay_rate

FROM (

    SELECT

        dt,

        SUM(
            CASE
                WHEN page_name = '首页'
                THEN 1
                ELSE 0
            END
        ) AS home_cnt,

        SUM(
            CASE
                WHEN page_name = '商品详情页'
                THEN 1
                ELSE 0
            END
        ) AS product_cnt,

        SUM(
            CASE
                WHEN page_name = '购物车'
                THEN 1
                ELSE 0
            END
        ) AS cart_cnt,

        SUM(
            CASE
                WHEN page_name = '结算页'
                THEN 1
                ELSE 0
            END
        ) AS pay_cnt

    FROM dwd_fact_user_event

    GROUP BY dt

) t;