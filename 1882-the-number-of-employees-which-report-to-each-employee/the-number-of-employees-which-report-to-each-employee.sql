with managers as (
    select age, reports_to 
    from employees
    where reports_to is not null
)

select e.employee_id, e.name, count(*) as reports_count, round(avg(m.age)) as average_age
from employees e
join managers m on m.reports_to = e.employee_id
group by e.employee_id, e.name
order by employee_id