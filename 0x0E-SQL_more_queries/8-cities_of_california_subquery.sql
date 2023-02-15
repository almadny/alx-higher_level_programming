-- lists all the cities of California in hbtn_0d_us
-- Create a query and subquery
SELECT *
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
);
