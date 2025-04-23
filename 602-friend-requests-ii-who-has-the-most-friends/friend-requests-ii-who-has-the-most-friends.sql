-- with diff_count as (
--     select accepter_id as id, count(accepter_id) as f_acc_count
--     from RequestAccepted
--     group by accepter_id

--     union all

--     select requester_id as id, count(requester_id) as f_req_count
--     from RequestAccepted
--     group by requester_id
-- ) 

-- select id, sum(f_acc_count) as num 
-- from diff_count
-- group by id
-- order by num desc
-- limit 1







with req as (
    select requester_id as id, count(*) as num
    from requestAccepted
    group by requester_id
),
accp as (
    select accepter_id as id, count(*) as num
    from requestAccepted
    group by accepter_id
)

select coalesce(r.id, a.id) as id, (coalesce(r.num, 0) + coalesce(a.num, 0)) as num
from req r
full outer join accp a on r.id = a.id
order by num desc
limit 1