-- Create second_table and insert records in hbtn_0c_0
-- This script creates a table if it doesn't exist and adds multiple rows with specific data

CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);

