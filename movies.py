SELECT * FROM movies


SELECT name, genre, year FROM movies


SELECT imdb_rating AS 'IMDb' FROM movies


SELECT DISTINCT year FROM movies


SELECT * FROM movies WHERE name LIKE 'Se_en'


SELECT * FROM movies WHERE name LIKE 'The %'


SELECT * FROM movies WHERE year BETWEEN 1970 and 1979


SELECT * FROM movies WHERE year < 1985 AND genre = 'horror'


SELECT * FROM movies WHERE genre = 'comedy' OR genre = 'romance'


SELECT name, year, imdb_rating FROM movies ORDER BY imdb_rating DESC


SELECT * FROM movies ORDER BY imdb_rating DESC
LIMIT 3


SELECT name,
   CASE
       WHEN genre = 'romance' THEN 'Chill'
        WHEN genre = 'comedy' THEN 'Chill'
        ELSE 'Intense'
    END AS 'Mood'
FROM movies
