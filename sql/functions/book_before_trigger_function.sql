create or replace function book_before_trigger_function()
returns trigger
language plpgsql
as $$

begin
    if (TG_OP = 'INSERT') then
        -- before insert 

    elseif (TG_OP = 'UPDATE') then
        -- before update

    elseif (TG_OP = 'DELETE') then
        -- before delete

        delete from book_authors ba where ba.book_id = OLD.bid;
        delete from book_genres bg where bg.book_id = OLD.bid;
        delete from book_review br where br.book_id = OLD.bid;


    end if;
    return NEW;
end; 
$$

