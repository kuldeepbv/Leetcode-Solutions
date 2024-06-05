select activity_date as day, count(distinct user_id) as active_users
from activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date














-- with assigned_row_numbers as (
--     select *,
--     row_number() over (partition by session_id) as row_num
--     from activity
-- )
-- select * from assigned_row_numbers

-- -- open_session_row_numbers as (
-- --     select user_id, activity_date, row_num
-- --     from assigned_row_numbers
-- --     where activity_type = 'open_session'
-- -- ),
-- -- end_session_row_numbers as (
-- --     select user_id, activity_date, row_num
-- --     from assigned_row_numbers
-- --     where activity_type = 'end_session'
-- -- )
-- -- select activity_date as day, count(distinct user_id) as active_users
-- -- from (
-- -- select * from open_session_row_numbers
-- -- union 
-- -- select * from end_session_row_numbers
-- -- ) 
-- -- group by activity_date
-- -- having 
-- -- select esrn.activity_date as day, count(osrn.user_id) as active_users 
-- -- from open_session_row_numbers osrn
-- -- join end_session_row_numbers esrn on osrn.user_id = esrn.user_id
-- -- where esrn.row_num - osrn.row_num > 1
-- -- group by esrn.activity_date

