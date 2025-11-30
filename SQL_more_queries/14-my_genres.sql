-- Script that lists all genres of the TV show Dexter
-- Each record shows tv_genres.name, sorted by name ascending
SELECT genres.name
FROM genres
JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
