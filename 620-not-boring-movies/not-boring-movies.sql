select *
from cinema
where description != 'boring' and id % 2 != 0
order by rating desc