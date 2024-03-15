-- Select the hbtn_0c_0 database for subsequent operations
USE hbtn_0c_0;

-- Convert database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the entire table to use the database's default character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Adjust the 'name' field to specify the collation explicitly
ALTER TABLE first_table CHANGE name name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
