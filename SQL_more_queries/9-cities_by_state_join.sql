-- Script that lists all cities in the database hbtn_0d_usa
-- Each record shows cities.id - cities.name - states.name, sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
