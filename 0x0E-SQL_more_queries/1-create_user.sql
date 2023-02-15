-- Create User
-- Create User 1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant privilege to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
