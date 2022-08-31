
create or replace function get_libraries()
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
    select * from library 
);
end;
$$