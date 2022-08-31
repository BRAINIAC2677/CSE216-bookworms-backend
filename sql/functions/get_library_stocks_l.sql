
create or replace function get_library_stocks(p_lid integer)
returns table(
    lsid integer,
    quantity integer,
    borrowed_fee_per_day integer,
    book_id integer,
    library_id integer
)
language plpgsql
as $$
begin
return query (
    select * from library_stock ls
    where ls.library_id = p_lid
);
end;
$$