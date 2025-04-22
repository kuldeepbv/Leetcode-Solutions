with users as (
    select user_id, session_id
    from activity
    group by user_id, session_id
    having count(*) > 0
)

select a.activity_date as day, count(distinct a.user_id) as active_users
from activity a
join users u on a.user_id = u.user_id and a.session_id = u.session_id
where a.activity_date between '2019-06-28' and '2019-07-27'
group by a.activity_date