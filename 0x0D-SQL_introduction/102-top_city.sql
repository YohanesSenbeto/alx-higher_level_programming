-- Import the table dump
SOURCE temperature_data.sql;

-- Display the state with the maximum temperature
SELECT state, MAX(temperature) AS max_temp
FROM temperature
GROUP BY state;
