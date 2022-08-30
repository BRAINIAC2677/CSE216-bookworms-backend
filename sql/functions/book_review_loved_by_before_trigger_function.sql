create or replace function book_review_loved_by_before_trigger_function()
returns trigger
language plpgsql
as $$
declare
    f_uid integer;
    t_uid integer;
    c_time timestamp with time zone;
begin 
    if (TG_OP = 'INSERT') then
        -- before insert

        -- notifying the reviewer that the book has been loved 
        SELECT NOW()
        INTO c_time;
        SELECT user_id 
        INTO f_uid 
        FROM reader 
        WHERE rid = NEW.reader_id;
        SELECT user_id
        INTO t_uid 
        FROM reader 
        WHERE rid = 
        (
            SELECT reviewer_id FROM book_review WHERE brid = NEW.bookreview_id
        );
        insert into notification (created_at, content_id, event_id, notification_from_id, notification_to_id) values (c_time,NEW.bookreview_id, 2, f_uid , t_uid);

    elseif (TG_OP = 'UPDATE') then
        -- before update

    elseif (TG_OP = 'DELETE') then
        -- before delete
    end if;
    return NEW;
end;
$$

