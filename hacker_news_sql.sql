/*Analyse data from Hacker News using SQL*/

 SELECT title, score FROM hacker_news ORDER BY 2 DESC LIMIT 5;

 SELECT user, SUM(score) AS 'Score' FROM hacker_news GROUP BY 1 HAVING Score > 200 ORDER BY Score DESC;

 SELECT (517 + 309 + 304 + 282) / 6366.0;

 SELECT user, COUNT(*) FROM hacker_news WHERE url LIKE '%watch?v=dQw4w9WgXcQ' GROUP BY user ORDER BY COUNT(*) DESC;


SELECT CASE 
  WHEN url LIKE '%github.com%' THEN 'Github'
  WHEN url LIKE '%medium.com%' THEN 'Medium'
  WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
  ELSE 'Other'
END AS 'Source', COUNT(*)
FROM hacker_news GROUP BY 1;

SELECT strftime('%H', timestamp) AS 'Hour', ROUND(AVG(score), 1) AS 'Ave_Score', COUNT(*) AS 'Num_Stories' FROM hacker_news WHERE Hour IS NOT NULL GROUP BY 1; 