DROP TABLE IF EXISTS dws_user_rfm;

CREATE TABLE dws_user_rfm AS

select

    user_id,

    max(order_time) as last_order_time,

    count(order_id) as frequency,

    sum(order_amount) as monetary

from dwd_fact_order_info

where pay_status = '已支付'

group by user_id