create or replace function get_book_reviews()
returns table(
    brid integer,
    rating integer,
    content text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    book_id integer,
    reviewer_id integer
)
language plpgsql
as $$
begin
    return query(
        select * from book_review
    );
end;
$$