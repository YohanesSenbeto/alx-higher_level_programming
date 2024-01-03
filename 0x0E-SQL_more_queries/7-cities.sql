-- create the hbtn_0d_usa database if does not exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to hbtn_0d_usa

USE hbtn_0d_usa;

-- create Table if does not exists

CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR (256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
