with managers as (
     select reports_to, count(*) as reports_count, round(avg(age)) as average_age
    from employees
    where reports_to is not null
    group by reports_to
)

select e.employee_id, e.name, m.reports_count, m.average_age
from managers m
join employees e on m.reports_to = e.employee_id
order by employee_id