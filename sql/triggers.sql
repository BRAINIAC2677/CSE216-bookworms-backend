-- before bookreview
CREATE OR REPLACE TRIGGER book_review_before_trigger 
BEFORE INSERT OR UPDATE OR DELETE
ON book_review 
FOR EACH ROW 
    EXECUTE PROCEDURE book_review_before_trigger_function();

-- before bookreview_loved_by
CREATE OR REPLACE TRIGGER book_review_loved_by_before_trigger
BEFORE INSERT OR UPDATE OR DELETE
ON book_review_loved_by
FOR EACH ROW
    EXECUTE PROCEDURE book_review_loved_by_before_trigger_function();

-- before comment
CREATE OR REPLACE TRIGGER comment_before_trigger 
BEFORE INSERT OR UPDATE OR DELETE 
ON comment 
FOR EACH ROW 
    EXECUTE PROCEDURE comment_before_trigger_function();

-- before comment_loved_by
CREATE OR REPLACE TRIGGER comment_loved_by_before_trigger
BEFORE INSERT OR UPDATE OR DELETE
ON comment_loved_by
FOR EACH ROW
    EXECUTE PROCEDURE comment_loved_by_before_trigger_function();

-- before friend
CREATE OR REPLACE TRIGGER friend_before_trigger
BEFORE INSERT OR UPDATE OR DELETE
ON friend
FOR EACH ROW
    EXECUTE PROCEDURE friend_before_trigger_function();

-- before read
CREATE OR REPLACE TRIGGER read_before_trigger
BEFORE INSERT OR UPDATE OR DELETE
ON read 
FOR EACH ROW 
    EXECUTE PROCEDURE read_before_trigger_function();

-- before bookborrow
CREATE OR REPLACE TRIGGER book_borrow_before_trigger 
BEFORE INSERT OR UPDATE OR DELETE
ON book_borrow
FOR EACH ROW 
    EXECUTE PROCEDURE book_borrow_before_trigger_function();
