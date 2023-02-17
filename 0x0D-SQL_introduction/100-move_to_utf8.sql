-- Convert Database to utf8
-- Select the database
USE hbtn_0c_0;
-- Convert Database
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- Convert Table
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- Convert column
ALTER TABLE first_table CHANGE 
name name VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;

