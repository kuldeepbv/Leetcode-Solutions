with count_tiv_2015 as (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(tiv_2015) > 1
),
updated as (
    select pid, tiv_2015, tiv_2016, (lat, lon) as lat_lon 
    from insurance
),
count_lat_lon as (
    select lat_lon
    from updated
    group by lat_lon
    having count(lat_lon) = 1
)

select round(sum(case when tiv_2015 in (select * from count_tiv_2015) and lat_lon in (select * from count_lat_lon) then tiv_2016 else 0 end)::numeric, 2) as tiv_2016
from updated u