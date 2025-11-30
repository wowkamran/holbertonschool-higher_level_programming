-- Script that lists all Comedy shows in the database hbtn_0d_tvshows
-- Each record shows tv_shows.title, sorted by title ascending
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
JOIN genres
ON tv_show_genres.genre_id = genres.id
WHERE genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
