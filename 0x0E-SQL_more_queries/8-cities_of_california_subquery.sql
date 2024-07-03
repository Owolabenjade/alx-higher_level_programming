-- This script lists all cities of California from the 'hbtn_0d_usa' database
-- The query uses a subquery to match 'state_id' with the 'id' of California in 'states'
-- Results are sorted in ascending order by 'cities.id'

SELECT id, name
FROM cities
WHERE state_id = (
  SELECT id
  FROM states
  WHERE name = 'California'
)
ORDER BY id ASC;

