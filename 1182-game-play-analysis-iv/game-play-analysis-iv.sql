with ranking_event_date as (
    select *,
    rank() over(partition by player_id order by event_date) as rnk
    from activity
),
first_log_in as (
    select player_id, event_date 
    from ranking_event_date 
    where rnk = 1
)

select round(count(fli.player_id) / (select count(distinct player_id) from activity)::numeric, 2) as fraction
from activity a
join first_log_in fli on a.player_id = fli.player_id 
where a.event_date - fli.event_date = 1