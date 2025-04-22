with log_in_rank as (
    select player_id, event_date,
    rank() over(partition by player_id order by event_date) as rnk
    from activity
)

select round(count(*) / (select count(distinct player_id) from activity)::numeric, 2) as fraction
from log_in_rank lir1
join log_in_rank lir2 on lir1.player_id = lir2.player_id and lir1.rnk = 1 and lir2.rnk = 2 and lir2.event_date - lir1.event_date = 1