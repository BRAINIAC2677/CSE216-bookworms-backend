
create or replace function get_notifications_uid(uid int)
returns table(
    nid integer,
    created_at timestamp with time zone,
    content_id integer,
    event_id integer,
    notification_from_id integer,
    notification_to_id integer
)
language plpgsql
as $$
begin
return query (
    select * from notification n
    where n.notification_to_id = uid
);
end;
$$