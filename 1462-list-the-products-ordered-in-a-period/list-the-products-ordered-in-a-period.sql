with month_orders as (
    select product_id, to_char(order_date, 'MM-YYYY') as month_year, unit
    from orders
),
sum_of_orders as (
    select product_id, sum(unit) as unit
    from month_orders
    where month_year = '02-2020'
    group by product_id
)

select p.product_name, so.unit
from products p
join sum_of_orders so on p.product_id = so.product_id
where so.unit >= 100