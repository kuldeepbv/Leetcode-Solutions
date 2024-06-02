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

-- select * 
-- from my_rank 
-- where event_date - (select event_date from my_rank where rnk = 1) = 1

-- with lagged_dates as (
--     select *, 
--     lag(event_date) over (partition by player_id order by event_date) as prev_event_date
--     from activity
-- ),
-- my_check as (
--     select player_id, count(player_id)
--     from lagged_dates
--     where event_date - prev_event_date = 1
--     group by player_id
-- )

-- select * from lagged_dates 

--select count(player_id) from my_check

-- select round(count(*) / (select count(distinct player_id) from activity)::numeric, 2) as fraction
-- from lagged_dates
-- where event_date - prev_event_date = 1