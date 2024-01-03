-- Connect to the MySQL server
mysql -h localhost -u root -p

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Get the state_id of California from the states table
SET @california_state_id := (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id ASC;
