
create or replace function get_libraries_b(p_bid integer)
returns table(
    lid integer, 
    library_name varchar(200),
    photo_urll varchar(200),
    longitude double precision,
    latitude double precision
)
language plpgsql
as $$
begin
return query (
    select * from library l
    where l.lid IN (
        select library_id 
        from library_stock ls
        where ls.book_id = p_bid
    )
);
end;
$$