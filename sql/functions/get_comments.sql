
create or replace function get_comments()
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
    select * from comment
);
end;
$$