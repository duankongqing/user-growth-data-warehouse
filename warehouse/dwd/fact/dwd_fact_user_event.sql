DROP TABLE IF EXISTS dwd_fact_user_event;

CREATE TABLE dwd_fact_user_event AS

SELECT
    event_id,
    user_id,
    event_time,
    event_type,
    page_name,
    device_type,

    CASE
        WHEN stay_duration < 0 THEN NULL
        ELSE stay_duration
    END AS stay_duration,

    DATE(event_time) AS dt

FROM (

    SELECT
        event_id,
        user_id,
        event_time,
        event_type,
        page_name,
        device_type,
        stay_duration,
        ROW_NUMBER() OVER (
            PARTITION BY event_id
            ORDER BY event_time DESC
        ) AS rn

    FROM ods_events

    WHERE event_type != 'test_event'

) t

WHERE rn = 1;