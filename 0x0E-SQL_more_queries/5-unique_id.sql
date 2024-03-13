-- This script creates the 'unique_id' table with an 'id' that is unique and has a default value of 1

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);

