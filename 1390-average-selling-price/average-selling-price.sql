select p.product_id, coalesce(round(sum(p.price * u.units) / sum(u.units)::numeric, 2), 0) as average_price
from prices p
left join unitssold u on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id