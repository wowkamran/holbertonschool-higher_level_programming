-- Script that lists all the cities of California in the database hbtn_0d_usa
-- Results are sorted in ascending order by cities.id
SELECT cities.id, cities.name, cities.state_id
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
