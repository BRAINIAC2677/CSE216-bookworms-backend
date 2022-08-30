create or replace function read_before_trigger_function()
returns trigger
language plpgsql
as $$
begin
    if (TG_OP = 'INSERT') then
        -- before insert 

        -- notifying the reader's friends
        call notifying_friends_proc(NEW.reader_id, NEW.rsid, 7);

    elseif (TG_OP = 'UPDATE') then
        -- before update

    elseif (TG_OP = 'DELETE') then
        -- before delete
    end if;
    return NEW;
end; 
$$

