-- Create a database and a table in it
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the created database
USE hbtn_0d_usa;
-- Ceeate a table in the database
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id)
		REFERENCES states (id),
	name VARCHAR(256) NOT NULL
);
