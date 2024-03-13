-- This script creates the 'hbtn_0d_usa' database (if it does not exist)
-- and the 'cities' table where 'state_id' is a foreign key referencing 'states.id'

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database
USE hbtn_0d_usa;

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);

