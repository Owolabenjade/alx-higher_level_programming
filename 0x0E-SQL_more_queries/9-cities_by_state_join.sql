-- This script lists all cities from the 'hbtn_0d_usa' database along with their state names
-- Displays 'cities.id', 'cities.name', and 'states.name' for each city
-- Results are sorted in ascending order by 'cities.id'
-- Utilizes an implicit JOIN between 'cities' and 'states' through the 'state_id' field

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

