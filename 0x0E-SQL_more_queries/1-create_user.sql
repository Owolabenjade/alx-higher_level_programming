-- This script creates user 'user_0d_1' and grants all privileges to this user

-- Attempt to create the user without error if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes made by the GRANT statement
FLUSH PRIVILEGES;

