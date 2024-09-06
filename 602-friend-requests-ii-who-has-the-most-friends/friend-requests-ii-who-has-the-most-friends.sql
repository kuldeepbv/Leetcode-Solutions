with diff_count as (
    select accepter_id as id, count(accepter_id) as f_acc_count
    from RequestAccepted
    group by accepter_id

    union all

    select requester_id as id, count(requester_id) as f_req_count
    from RequestAccepted
    group by requester_id
) 

select id, sum(f_acc_count) as num 
from diff_count
group by id
order by num desc
limit 1