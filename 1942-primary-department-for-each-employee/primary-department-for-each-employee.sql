with dept_count as (
    select employee_id, count(*) as cnt
    from employee
    group by employee_id
)

select dc.employee_id, e.department_id
from dept_count dc
join employee e on dc.employee_id = e.employee_id
where (dc.cnt = 1 or e.primary_flag = 'Y')