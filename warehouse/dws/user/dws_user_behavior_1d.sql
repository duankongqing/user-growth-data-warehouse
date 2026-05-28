DROP TABLE IF EXISTS dws_user_behavior_1d;

CREATE TABLE dws_user_behavior_1d AS

SELECT

    dt,

    COUNT(DISTINCT user_id) AS dau,

    COUNT(*) AS total_events,

    SUM(
        CASE
            WHEN event_type = 'page_view' THEN 1
            ELSE 0
        END
    ) AS page_view_cnt,

    SUM(
        CASE
            WHEN event_type = 'click' THEN 1
            ELSE 0
        END
    ) AS click_cnt,

    SUM(
        CASE
            WHEN event_type = 'purchase_click' THEN 1
            ELSE 0
        END
    ) AS purchase_click_cnt,

    AVG(stay_duration) AS avg_stay_duration

FROM dwd_fact_user_event

GROUP BY dt;