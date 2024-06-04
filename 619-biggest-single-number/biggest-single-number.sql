with all_counts as (
    select num
    from mynumbers
    group by num
    having count(num) = 1
)

select max(num) as num
from all_counts