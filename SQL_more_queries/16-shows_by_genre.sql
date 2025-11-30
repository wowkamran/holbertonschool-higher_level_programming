-- Script that lists all shows and their genres in the database hbtn_0d_tvshows
-- Display NULL for shows without a genre
-- Each record shows tv_shows.title - tv_genres.name, sorted by title and genre name
SELECT tv_shows.title, genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN genres
ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title ASC, genres.name ASC;
