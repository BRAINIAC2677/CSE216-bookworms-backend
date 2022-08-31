
create or replace function get_library_stocks()
returns table(
    lsid integer,
    quantity integer,
    borrowed_fee_per_day integer,
    book_id varchar(13),
    library_id integer
)
language plpgsql
as $$
begin
return query (
    select * from library_stock
);
end;
$$