DROP TABLE IF EXISTS dws_user_retention_1d;

CREATE TABLE dws_user_retention_1d AS

SELECT

    a.dt AS register_dt,

    COUNT(DISTINCT a.user_id) AS register_user_cnt,

    COUNT(DISTINCT b.user_id) AS retention_user_cnt,

    ROUND(
        COUNT(DISTINCT b.user_id) * 1.0
        / NULLIF(COUNT(DISTINCT a.user_id), 0),
        2
    ) AS retention_rate

FROM dwd_dim_user_info a

LEFT JOIN dwd_fact_user_event b
    ON a.user_id = b.user_id
    AND DATEDIFF(b.dt, a.dt) = 1

GROUP BY register_dt;