-- List the number of records with the same score in second_table
-- Results are sorted by the count of records per score in descending order

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC, score DESC;

