-- Script that lists all records of second_table with non-empty name
-- Display score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
