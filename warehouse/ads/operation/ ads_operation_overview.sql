DROP TABLE IF EXISTS ads_operation_overview;

CREATE TABLE ads_operation_overview AS

SELECT

    a.dt,
    a.dau,
    b.total_gmv,
    b.order_cnt,
    c.retention_rate

FROM dws_user_behavior_1d a

LEFT JOIN dws_order_trade_1d b
ON a.dt = b.dt

LEFT JOIN dws_user_retention_1d c
on a.dt = c.register_dt;