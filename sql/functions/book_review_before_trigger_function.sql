create or replace function book_review_before_trigger_function()
returns trigger
language plpgsql
as $$
begin
    if (TG_OP = 'INSERT') then
        -- before insert 

        -- notifying reviewer's friends
        call notifying_friends_proc(NEW.reviewer_id, NEW.brid, 1);

       -- increasing reviewer's reputation
        UPDATE reader SET reputation = reputation + 10 WHERE rid = NEW.reviewer_id;

    elseif (TG_OP = 'UPDATE') then
        -- before update

    elseif (TG_OP = 'DELETE') then
        -- before delete
    end if;
    return NEW;
end; 
$$

