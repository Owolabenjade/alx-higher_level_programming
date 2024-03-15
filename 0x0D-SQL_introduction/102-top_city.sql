-- Display the top 3 cities by average temperature during July and August
-- The results are ordered by temperature in descending order

SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

