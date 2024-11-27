with year_rank as (
    select *,
    rank() over(partition by product_id order by year) as ranked_year
    from sales
)

select product_id, year as first_year, quantity, price
from year_rank
where ranked_year = 1