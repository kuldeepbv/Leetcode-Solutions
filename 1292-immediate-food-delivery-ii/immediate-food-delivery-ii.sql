with first_order as (
    select delivery_id, customer_id, order_date, customer_pref_delivery_date, rank() over(partition by customer_id order by order_date) as rnk
    from delivery
),
all_percent as (
select round(((sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) * 100)/ count(*))::numeric, 2) as immediate_percent
from first_order
where rnk = 1
group by customer_id
)

select round(avg(immediate_percent)::numeric, 2) as immediate_percentage 
from all_percent 