with all_sub as (
    select *
    from students
    cross join subjects
)

select als.student_id, als.student_name, als.subject_name, count(e.student_id) as attended_exams
from all_sub als
left join examinations e on als.student_id = e.student_id and als.subject_name = e.subject_name
group by als.student_id, als.student_name, als.subject_name