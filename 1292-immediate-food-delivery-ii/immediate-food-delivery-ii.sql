with order_nums as (
    select *,
    rank() over(partition by customer_id order by order_date) as order_num
    from delivery
)

select round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100 / count(*)::numeric, 2) as immediate_percentage
from order_nums
where order_num = 1