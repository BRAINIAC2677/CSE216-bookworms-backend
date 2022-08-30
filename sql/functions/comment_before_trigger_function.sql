create or replace function comment_before_trigger_function()
returns trigger
language plpgsql
as $$
begin
    if (TG_OP = 'INSERT') then
        -- before insert 

        -- notifying the commenter's friends 
        call notifying_friends_proc(NEW.commented_by_id, NEW.cid, 3);

    elseif (TG_OP = 'UPDATE') then
        -- before update

    elseif (TG_OP = 'DELETE') then
        -- before delete
    end if;
    return NEW;
end; 
$$

