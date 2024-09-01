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

-- select p.product_name, sum(o.unit) as unit
-- from products p
-- join orders o on p.product_id = o.product_id
-- where to_char(order_date, 'MM-YYYY') = '02-2020'
-- group by p.product_name
-- --having unit >= 100