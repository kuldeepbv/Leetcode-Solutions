(select u.name as results
from movierating mr
join users u on mr.user_id = u.user_id
group by u.name
order by count(*) desc, u.name
limit 1)

union all

(select m.title as results
from movierating mr
join movies m on mr.movie_id = m.movie_id
where to_char(mr.created_at, 'YYYY-MM') = '2020-02'
group by m.title
order by avg(mr.rating) desc, m.title
limit 1)