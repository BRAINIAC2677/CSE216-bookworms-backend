create or replace procedure notifying_friends_proc(
    p_rid integer,
    p_content_id integer,
    p_event_id integer
)
language plpgsql
as $$
declare
    f_uid integer;
    t_uid integer;
    c_time timestamp with time zone;
begin 
    SELECT NOW() 
    INTO c_time;
    SELECT user_id 
    INTO f_uid 
    FROM reader 
    WHERE rid = p_rid;
    for t_uid in (
        SELECT user_id FROM reader WHERE rid IN (
            (
                SELECT friendship_from_id 
                FROM friend
                WHERE (NOT is_pending) 
                AND (friendship_to_id = p_rid)
            )
            UNION
            (
                SELECT friendship_to_id 
                FROM friend
                WHERE (NOT is_pending) 
                AND (friendship_from_id = p_rid)
            )
        )
    )
    loop
        insert into notification (created_at, content_id, event_id, notification_from_id, notification_to_id) values (c_time, p_content_id, p_event_id, f_uid , t_uid);
    end loop;
end;
$$
