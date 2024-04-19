-- Write your PostgreSQL query statement below

with machine_start as (
    select machine_id, process_id, timestamp as timestamp_start
    from activity
    where activity_type = 'start'
), 
machine_end as (
    select machine_id, process_id, timestamp as timestamp_end
    from activity
    where activity_type = 'end'
)

select ms.machine_id, round(avg(me.timestamp_end - ms.timestamp_start)::numeric, 3) as processing_time 
from machine_start ms
join machine_end me on ms.machine_id = me.machine_id and    
                       ms.process_id = me.process_id
group by ms.machine_id