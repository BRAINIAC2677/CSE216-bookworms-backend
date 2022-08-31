create or replace function book_borrow_before_trigger_function()
returns trigger
language plpgsql
as $$
declare
    f_uid integer;
    f_rid integer;
    t_lid integer;
    t_uid integer;
    c_time timestamp with time zone;
begin
    if (TG_OP = 'INSERT') then
        -- before insert 

        -- notifying the library from which the book is borrowed
        f_rid:=NEW.borrowed_by_id;
        SELECT NOW()
        INTO c_time;
        SELECT user_id 
        INTO f_uid 
        FROM reader 
        WHERE rid = f_rid;
        t_lid:=NEW.borrowed_from_id;
        SELECT user_id 
        INTO t_uid 
        FROM library 
        WHERE lid = t_lid;
        insert into notification (created_at,content_id, event_id, notification_from_id, notification_to_id) values (c_time,NEW.bbid, 9 , f_uid , t_uid);

        -- increasing the reputation of the reader who borrowed the book
        UPDATE reader SET reputation = reputation + 5 WHERE rid = f_rid;

    elseif (TG_OP = 'UPDATE') then
        -- before update

    elseif (TG_OP = 'DELETE') then
        -- before delete
    end if;
    return NEW;
end; 
$$

