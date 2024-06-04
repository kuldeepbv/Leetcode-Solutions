with ranked_years as (
    select *,
    rank() over (partition by product_id order by year) as rnk_year
    from sales
)

select product_id, year as first_year, quantity, price 
from ranked_years
where rnk_year = 1