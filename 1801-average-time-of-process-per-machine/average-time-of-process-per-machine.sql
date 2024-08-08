with activity_start as (
    select machine_id, process_id, activity_type, timestamp
    from activity
    where activity_type = 'start'
),
activity_end as (
    select machine_id, process_id, activity_type, timestamp
    from activity
    where activity_type = 'end'
)

select act_st.machine_id, round(avg(act_en.timestamp - act_st.timestamp)::numeric, 3) as processing_time
from activity_start act_st
join activity_end act_en on act_st.machine_id = act_en.machine_id and act_st.process_id = act_en.process_id
group by act_st.machine_id