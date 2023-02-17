-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS name
FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT tv_show_genres.genre_id
	FROM tv_show_genres
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter"
)
ORDER BY tv_genres.name;
