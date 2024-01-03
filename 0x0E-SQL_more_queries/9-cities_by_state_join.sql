-- Connect to the MySQL server
mysql -h localhost -uroot -p

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List all cities with their corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
