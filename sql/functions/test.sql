create or replace function get_books()
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
return query select * from book;
end;

create or replace function get_bookreviews()
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
return query select * from book_review;
end;
$$;

