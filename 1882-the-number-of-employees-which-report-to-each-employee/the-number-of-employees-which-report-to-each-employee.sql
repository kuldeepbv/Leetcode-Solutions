with managers as (
    select reports_to, age 
    from employees 
    where reports_to is not null
)

select e.employee_id, e.name, count(*) as reports_count, round(avg(m.age)) as average_age
from managers m
left join employees e on m.reports_to = e.employee_id
group by e.employee_id, e.name
order by e.employee_id