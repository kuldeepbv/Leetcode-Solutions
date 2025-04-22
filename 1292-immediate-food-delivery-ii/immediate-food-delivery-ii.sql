with order_rnk as (
    select *,
    rank() over(partition by customer_id order by order_date) as rnk
    from delivery
)

select round(count(*) * 100.0 / (select count(distinct customer_id) from delivery)::numeric, 2) as immediate_percentage
from order_rnk
where order_date = customer_pref_delivery_date and rnk = 1