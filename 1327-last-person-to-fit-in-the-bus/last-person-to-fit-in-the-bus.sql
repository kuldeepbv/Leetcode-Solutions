with cum_sum as (
    select person_name, turn,
    sum(weight) over(order by turn) as cum_weight
    from queue
)

select person_name
from cum_sum
where cum_weight <= 1000
order by turn desc
limit 1