-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT DISTINCT(tv_show_genres.show_id)
	FROM tv_show_genres
	INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = "Comedy"
)
ORDER BY tv_shows.title;
