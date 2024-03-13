-- This script creates the 'hbtn_0d_usa' database and 'states' table

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Create the 'states' table if it does not exist
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
  name VARCHAR(256) NOT NULL
);

