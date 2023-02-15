-- Convert Database to utf8
-- Convert Database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert Table
-- Make table row dynamic
ALTER TABLE second_table ROW_FORMAT=DYNAMIC;
-- Convert Table
ALTER TABLE second_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

