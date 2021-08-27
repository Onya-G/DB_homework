SELECT name, year FROM albums
	WHERE year = 2018;
SELECT name, time FROM tracks
	ORDER BY time DESC 
	LIMIT 1;
SELECT name, time FROM tracks
	WHERE time >= 210;
SELECT name, year FROM mixtapes
	WHERE year BETWEEN 2018 AND 2020;
SELECT name FROM musicians
	WHERE name NOT LIKE '% %';
SELECT name FROM tracks
	WHERE name ILIKE '%my%';
	