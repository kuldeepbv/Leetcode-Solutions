with prod_rnk as (
    select *,
    dense_rank() over(partition by product_id order by year) as rnk  
    from sales
)

select pr.product_id, pr.year as first_year, pr.quantity, pr.price
from product p 
join prod_rnk pr on p.product_id = pr.product_id
where pr.rnk = 1
