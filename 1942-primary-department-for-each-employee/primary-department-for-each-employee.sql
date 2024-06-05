with department_count as (
    select employee_id, count(*) as dpt_cnt
    from employee
    group by employee_id
)

select e.employee_id, e.department_id
from employee e
join department_count dc on e.employee_id = dc.employee_id
where dc.dpt_cnt = 1 or e.primary_flag = 'Y'