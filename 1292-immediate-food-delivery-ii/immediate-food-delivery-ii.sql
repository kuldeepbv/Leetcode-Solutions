with first_order as (
    select *, rank() over (partition by customer_id order by order_date) as order_num
    from delivery
)

select round(avg(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100::numeric, 2) as immediate_percentage
from first_order
where order_num = 1