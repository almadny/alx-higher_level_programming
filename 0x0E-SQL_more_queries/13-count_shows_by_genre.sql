-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_genres.name AS name, count(*) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
