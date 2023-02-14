-- List number rexord by the same score
-- List score
SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
