with rankings as (
    select *, rank() over(partition by email order by id) as rn
    from person
)

delete from person
where id in (select id from rankings where rn > 1)