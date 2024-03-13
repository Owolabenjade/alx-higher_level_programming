-- This script creates the 'id_not_null' table with 'id' defaulting to 1 and 'name'

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);

