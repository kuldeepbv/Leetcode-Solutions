with prod_rnk as (
    select *,
    dense_rank() over(partition by product_id order by year) as rnk  
    from sales
)

select product_id, year as first_year, quantity, price
from prod_rnk
where rnk = 1