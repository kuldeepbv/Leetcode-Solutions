select s.user_id, round(avg(case when action = 'confirmed' then 1 else 0 end)::numeric, 2) as confirmation_rate
from signups s
left join confirmations c on s.user_id = c.user_id
group by s.user_id