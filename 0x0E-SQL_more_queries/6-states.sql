-- Create the hbtn_0d_usa if does not Exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;
-- Create the states table if does not exists

CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR (256) NOT NULL
);
