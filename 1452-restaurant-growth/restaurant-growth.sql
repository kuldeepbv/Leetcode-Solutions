with skip_6_days as (
    select distinct visited_on
    from customer
    order by visited_on
    offset 6
)

select sd.visited_on, sum(c.amount) as amount, round(sum(c.amount)/7::numeric, 2) as average_amount
from skip_6_days sd
join customer c on c.visited_on between sd.visited_on - 6 and sd.visited_on
group by sd.visited_on
order by sd.visited_on 