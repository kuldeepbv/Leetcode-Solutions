with cum_sum as (
    select person_id, person_name, turn, sum(weight) over (order by turn) as added_sum
    from queue
)

select person_name 
from cum_sum
where added_sum <= 1000
order by turn desc
limit 1