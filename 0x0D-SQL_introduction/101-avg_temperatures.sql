-- Display the average temperature by city, ordered by descending temperature
-- This aggregates temperature data by city and orders the result by the average temperature

SELECT city, AVG(temperature) AS avg_temp FROM temperature_data GROUP BY city ORDER BY avg_temp DESC;

