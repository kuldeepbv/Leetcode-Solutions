with all_sub as (
    select *
    from students
    cross join subjects
)

select all_sub.student_id, all_sub.student_name, all_sub.subject_name, count(e.subject_name) as attended_exams
from all_sub
left join examinations e on all_sub.student_id = e.student_id and all_sub.subject_name = e.subject_name
group by all_sub.student_id, all_sub.student_name, all_sub.subject_name
order by all_sub.student_id