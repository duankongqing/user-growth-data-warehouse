DROP TABLE IF EXISTS dws_traffic_page_1d;

CREATE TABLE dws_traffic_page_1d AS

SELECT

    dt,

    page_name,

    COUNT(*) AS pv,

    COUNT(DISTINCT user_id) AS uv

FROM dwd_fact_user_event

GROUP BY dt, page_name;