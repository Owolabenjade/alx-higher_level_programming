-- This script creates the 'hbtn_0d_2' database and 'user_0d_2' user
-- 'user_0d_2' will have only SELECT privileges on 'hbtn_0d_2'

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it does not exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;

