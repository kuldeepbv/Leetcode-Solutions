with all_subject as(
    select st.student_id, st.student_name, su.subject_name
    from students st, subjects su
)

select a.student_id, a.student_name, a.subject_name, count(e.subject_name) as attended_exams
from all_subject a
left join examinations e on a.student_id = e.student_id and a.subject_name = e.subject_name
group by a.student_id, a.student_name, a.subject_name
order by a.student_id, a.student_name