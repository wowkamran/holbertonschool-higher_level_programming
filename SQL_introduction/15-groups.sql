-- Script that lists the number of records with the same score in second_table
-- Display score and count of records as 'number', ordered by number descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
