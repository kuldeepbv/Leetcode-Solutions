select (case 
    when id % 2 != 0 and id = (select max(id) from seat) then id
    when id % 2 != 0 then id + 1
    else id - 1 end) as id, student
from seat
order by id