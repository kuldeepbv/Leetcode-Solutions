with year_ranking as (
    select product_id, year,
    rank() over(partition by product_id order by year) as rank_of_years,
    quantity, price
    from sales
)

select product_id, year as first_year, quantity, price
from year_ranking
where rank_of_years = 1