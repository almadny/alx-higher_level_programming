-- lists all the cities of California in hbtn_0d_usa
-- Create a query and subquery
SELECT *
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
)
ORDER BY cities.id ASC;
