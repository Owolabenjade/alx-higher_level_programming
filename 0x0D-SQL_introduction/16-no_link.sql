-- List all records from second_table where the name is not null
-- Results display the score and the name, ordered by descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

