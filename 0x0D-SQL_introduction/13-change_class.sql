-- Remove records with a score <= 5 from second_table
-- This script aims to delete low-scoring records without affecting others

DELETE FROM second_table WHERE score <= 5;

