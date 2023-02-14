-- List not Null
-- List all records except those with Null Value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
