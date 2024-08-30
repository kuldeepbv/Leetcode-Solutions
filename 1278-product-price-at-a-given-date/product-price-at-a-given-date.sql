with prod as (
    select distinct product_id from products
),
product_prices as (
    select *, rank() over (partition by product_id order by change_date desc) as rn
    from products
    where change_date <= '2019-08-16'
)

select p.product_id, coalesce(pp.new_price, 10) as price
from prod p
left join product_prices pp on p.product_id = pp.product_id
where pp.rn = 1 or pp.rn is null