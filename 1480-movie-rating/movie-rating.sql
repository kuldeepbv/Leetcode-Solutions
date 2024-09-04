with cts as (
    select user_id, count(*) as cnt
    from movierating
    group by user_id
),
feb_ratings as (
    select movie_id, avg(rating) as rt
    from movierating
    where to_char(created_at, 'MM-YYYY') = '02-2020'
    group by movie_id
)

select min(users.name) as results
from cts 
join users on cts.user_id = users.user_id
where cts.cnt = (select max(cnt) from cts)

union all

select min(mv.title) as results
from feb_ratings fr
join movies mv on fr.movie_id = mv.movie_id
where fr.rt = (select max(rt) from feb_ratings)