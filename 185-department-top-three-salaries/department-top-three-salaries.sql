with salary_rank as (
    select *, 
    dense_rank() over(partition by departmentid order by salary desc) as rnk_salary
    from employee
)

select d.name as department, sr.name as employee, sr.salary 
from salary_rank sr
join department d on sr.departmentid = d.id
where sr.rnk_salary < 4