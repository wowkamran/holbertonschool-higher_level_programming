-- Script that lists all TV shows with their genre_id, including shows without a genre
-- Each record shows tv_shows.title - tv_show_genres.genre_id
-- Results sorted by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
