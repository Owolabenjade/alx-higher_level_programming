-- Update the score for Bob to 10 in second_table
-- This script uses Bob's name to locate the record, without relying on the ID

UPDATE second_table SET score = 10 WHERE name = 'Bob';

