select query_name, round(sum(round(rating / position::numeric, 100)) / count(*)::numeric, 2) as quality, round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*)::numeric, 2) as poor_query_percentage 
from queries 
where query_name is not null
group by query_name