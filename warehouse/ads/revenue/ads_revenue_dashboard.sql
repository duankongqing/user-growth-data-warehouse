DROP TABLE IF EXISTS ads_revenue_dashboard;

CREATE TABLE ads_revenue_dashboard AS

SELECT
    dt,
    order_cnt,
    total_gmv,
    avg_order_amount,
    paid_order_cnt
FROM dws_order_trade_1d