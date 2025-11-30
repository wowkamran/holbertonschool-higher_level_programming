-- Script that lists all genres and the number of shows linked to each
-- Each record shows genre - number_of_shows
-- Only display genres with at least one show, sorted by number_of_shows descending
SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
