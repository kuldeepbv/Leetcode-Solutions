with activity_start as (
    select * 
    from activity
    where activity_type = 'start'
),
activity_end as (
    select * 
    from activity
    where activity_type = 'end'
)

select ae.machine_id, round(avg(ae.timestamp - act_st.timestamp)::numeric, 3) as processing_time
from activity_start act_st
join activity_end ae on act_st.machine_id = ae.machine_id and act_st.process_id = ae.process_id
group by ae.machine_id