-- Create a database and a table in it
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the created database
USE hbtn_0d_usa;
-- Ceeate a table in the database
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
