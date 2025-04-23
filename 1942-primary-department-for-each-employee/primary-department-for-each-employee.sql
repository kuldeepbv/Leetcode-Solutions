with dept_count as (
    select employee_id, count(*) as cnt
    from employee
    group by employee_id
)

(select e.employee_id, e.department_id
from employee e
join dept_count dc on e.employee_id = dc.employee_id and dc.cnt > 1 and e.primary_flag = 'Y'

union

select e.employee_id, e.department_id
from employee e
join dept_count dc on e.employee_id = dc.employee_id and dc.cnt = 1)
order by employee_id