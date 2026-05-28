DROP TABLE IF EXISTS ads_user_growth_dashboard;

CREATE TABLE ads_user_growth_dashboard AS

SELECT

    a.dt,

    a.dau,

    a.total_events,

    a.page_view_cnt,

    a.avg_stay_duration,

    b.register_user_cnt,

    b.retention_rate

FROM dws_user_behavior_1d a

LEFT JOIN dws_user_retention_1d b
ON a.dt = b.register_dt;