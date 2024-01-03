-- Create Database hbtn_0c_0
-- Description: This script creates the database hbtn_0c_0 if it does not already exist.

USE mysql; -- Replace 'mysql' with the database you want to use, e.g., 'information_schema'
DELIMITER $$
CREATE PROCEDURE CreateIfNotExists()
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLSTATE '42S02' BEGIN END;
    CREATE DATABASE hbtn_0c_0;
END $$
DELIMITER ;

-- Call the stored procedure
CALL CreateIfNotExists();


