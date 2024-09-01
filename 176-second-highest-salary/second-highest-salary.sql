with highest_salary as (
    select id, rank() over(order by salary desc) as rnk
    from employee
)

select max(salary) as secondhighestsalary
from employee
where id not in (select id from highest_salary where rnk = 1)