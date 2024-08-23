with department_count as (
    select employee_id, count(*) as departments
    from employee
    group by employee_id
)
-- final_query as (
--     select dc.employee_id, (case when dc.departments = 1 then e.    department_id else case when e.primary_flag = 'Y' then e.department_id end end) as department_id
--     from department_count dc
--     join employee e on dc.employee_id = e.employee_id
-- )

-- select *
-- from final_query
-- where department_id is not null

select dc.employee_id, e.department_id
from department_count dc
join employee e on dc.employee_id = e.employee_id
where (dc.departments = 1 or e.primary_flag = 'Y') and e.department_id is not null