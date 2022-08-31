create or replace function get_book_reviews_b(p_bid integer)
returns table(
    brid integer,
    rating integer,
    content text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    book_id varchar(13),
    reviewer_id integer
)
language plpgsql
as $$
begin
    return query(
        select * from book_review br
        where br.book_id = p_bid
    );
end;
$$