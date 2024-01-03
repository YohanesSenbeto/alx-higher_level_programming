-- Import the table dump
SOURCE temperature_data.sql;

-- Calculate the average temperature (Fahrenheit) by city
SELECT city, AVG(temperature) AS average_temperature
FROM temperature
GROUP BY city
ORDER BY average_temperature DESC;
