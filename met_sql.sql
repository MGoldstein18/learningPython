/*Analysis of data from the Metropolitan Museum of Art */
 SELECT * FROM met LIMIT 10;

 SELECT COUNT(*) FROM met;

 SELECT COUNT(*) FROM met WHERE category LIKE '%celery%';

SELECT MIN(date) FROM met;

SELECT title, medium FROM met WHERE date like '%1600%';

SELECT country, COUNT(*) FROM met GROUP BY country ORDER BY 2 DESC LIMIT 10;

SELECT category, COUNT(*) FROM met GROUP BY 1 HAVING COUNT(*) > 100;

SELECT CASE
  WHEN medium LIKE "%gold%" THEN 'Gold'
  WHEN medium LIKE '%silver%' THEN 'Silver'
  Else NULL
END AS 'Bling', 
COUNT(*)
FROM met WHERE Bling IS NOT NULL GROUP BY 1 ORDER BY 2 DESC;