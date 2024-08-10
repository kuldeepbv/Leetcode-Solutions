select query_name, round(avg(round(rating / position::numeric, 10))::numeric, 2) as quality, round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*)::numeric, 2) as poor_query_percentage 
from queries 
where query_name is not null
group by query_name

-- SELECT query_name,
--     ROUND(AVG(1.0 * rating / position), 2) AS quality,
--     ROUND(COUNT(CASE WHEN rating < 3 THEN 1 ELSE NULL END) * 100.0 / COUNT(rating), 2) AS poor_query_percentage
-- FROM queries
-- GROUP BY query_name