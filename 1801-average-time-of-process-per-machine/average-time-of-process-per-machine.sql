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

select acs.machine_id, round(avg(ace.timestamp - acs.timestamp)::numeric, 3) as processing_time
from activity_start acs
join activity_end ace on acs.machine_id = ace.machine_id and acs.process_id = ace.process_id
group by acs.machine_id