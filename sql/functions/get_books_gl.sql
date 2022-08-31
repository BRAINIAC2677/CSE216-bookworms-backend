create or replace function get_books_gl(p_gte_page_count integer, p_lte_page_count integer)
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
    where b.page_count >= p_gte_page_count
    and b.page_count <= p_lte_page_count
);
end;
$$