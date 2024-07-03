-- This script creates the 'force_name' table with 'id' and 'name' columns

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);

