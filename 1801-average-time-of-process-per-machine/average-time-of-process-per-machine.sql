with activity_start as (
    select machine_id, process_id, timestamp
    from activity
    where activity_type = 'start'
),
activity_end as (
    select machine_id, process_id, timestamp
    from activity
    where activity_type = 'end'
)

select act_st.machine_id, round(avg(ae.timestamp - act_st.timestamp)::numeric, 3) as processing_time
from activity_start act_st
join activity_end ae on act_st.machine_id = ae.machine_id and act_st.process_id = ae.process_id
group by act_st.machine_id