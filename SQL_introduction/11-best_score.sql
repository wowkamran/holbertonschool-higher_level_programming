-- Script that lists all records with score >= 10 in second_table
-- Results display score and name, ordered by score descending
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
