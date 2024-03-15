-- List all records with a score >= 10 from second_table
-- Results are ordered by score in descending order and display score and name

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

