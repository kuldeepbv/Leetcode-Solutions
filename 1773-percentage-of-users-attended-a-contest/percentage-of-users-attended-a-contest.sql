select contest_id, round((count(*) * 100) / (select distinct count(*) from users) ::numeric, 2) as percentage
from register
group by contest_id
order by percentage desc, contest_id asc