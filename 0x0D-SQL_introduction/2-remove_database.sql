-- Delete Database hbtn_0c_0 If It Exists.
-- Description: This script deletes the database hbtn_0c_0 if it exists, without failing if it doesn't.

-- Create a stored procedure to delete the database
DELIMITER $$
CREATE PROCEDURE DeleteIfExists()
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLSTATE '42000' BEGIN END;
    DROP DATABASE hbtn_0c_0;
END $$
DELIMITER ;

-- Call the stored procedure to delete the database if it exists
CALL DeleteIfExists();

