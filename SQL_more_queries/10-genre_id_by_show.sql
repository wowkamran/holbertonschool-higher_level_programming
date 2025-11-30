-- script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record displays tv_shows.title - tv_show_genres.genre_id.
-- Results sortes in ascending order by tv_shows.title and tv_show_genres.genre_id
-- It uses only one SELECT statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
