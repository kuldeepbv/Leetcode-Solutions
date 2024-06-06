with managers as (
    select reports_to, count(reports_to) as reports_count, round(avg(age)) as average_age
    from employees
    where reports_to is not null
    group by reports_to
)

select m.reports_to as employee_id, e.name, m.reports_count, m.average_age
from managers m
join employees e on m.reports_to = e.employee_id
order by employee_id

--select * from managers
--select employee_id, name, reports_count
--from employees