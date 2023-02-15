-- Create a user and a database
-- Create a database named hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user named user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant user_0d_2 select privilege on the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
