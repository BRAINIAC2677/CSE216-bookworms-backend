create or replace function get_books_g(p_gte_page_count integer)
returns table(
    bid varchar(13),
    title varchar(255),
    description text,
    photo_url varchar(255),
    page_count int,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
)
language plpgsql
as $$
begin
return query (
    select *
    from book b
    where page_count >= p_gte_page_count
);
end;
$$