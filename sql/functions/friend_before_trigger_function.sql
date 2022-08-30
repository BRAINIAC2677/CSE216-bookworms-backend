create or replace function friend_before_trigger_function()
returns trigger
language plpgsql
as $$
declare
    f_uid integer;
    f_rid integer;
    t_uid integer;
begin
    if (TG_OP = 'INSERT') then
        -- before insert 

        -- got friend request
        f_rid:=NEW.friendship_from_id;
        SELECT user_id 
        INTO f_uid 
        FROM reader 
        WHERE rid = f_rid;
        SELECT user_id 
        INTO t_uid 
        FROM reader 
        WHERE rid = NEW.friendship_to_id;
        insert into notification (content_id, event_id, notification_from_id, notification_to_id) values (NEW.fid, 5, f_uid , t_uid);

    elseif (TG_OP = 'UPDATE') then
        -- before update

        -- friend request got accepted
        if (OLD.is_pending) and (NOT NEW.is_pending) then
            f_rid:=NEW.friendship_to_id;
            SELECT user_id 
            INTO f_uid 
            FROM reader 
            WHERE rid = f_rid;
            SELECT user_id 
            INTO t_uid 
            FROM reader 
            WHERE rid = NEW.friendship_from_id;
            insert into notification (content_id, event_id, notification_from_id, notification_to_id) values (NEW.fid,6, f_uid , t_uid);
        end if; 

    elseif (TG_OP = 'DELETE') then
        -- before delete
    end if;
    return NEW;
end; 
$$

