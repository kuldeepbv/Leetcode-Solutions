with ranked_login as (
    select player_id, event_date, rank() over(partition by player_id order by event_date) as login_rank
    from activity
)

select round(sum(case when rl1.event_date+1 = rl2.event_date then 1 else 0 end) / (select count(distinct player_id) from activity)::numeric, 2) as fraction 
from ranked_login rl1
left join ranked_login rl2 on rl1.player_id = rl2.player_id and rl1.login_rank = 1 and rl2.login_rank = 2