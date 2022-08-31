
create or replace function get_comments_r(p_rid integer)
returns table(
    cid integer,
    content text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    commented_by_id integer,
    commented_on_id integer
)
language plpgsql
as $$
begin
return query (
    select * from comment c
    where c.commented_by_id = p_rid
);
end;
$$