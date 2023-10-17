-- Create Table first_table If Not Exists
-- Description: This script creates the 'first_table' if it does not already exist in the current database.

DELIMITER $$
CREATE PROCEDURE CreateTableIfNotExists(IN dbName VARCHAR(100))
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLSTATE '42S01' BEGIN END;
    SET @db = dbName;
    SET @query = CONCAT('USE ', @db);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    CREATE TABLE IF NOT EXISTS first_table (
        id INT,
        name VARCHAR(256)
    );
END $$
DELIMITER ;

