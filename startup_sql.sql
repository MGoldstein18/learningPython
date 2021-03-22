/*SQL queries to get information from a database of data about startups. */

SELECT * FROM startups;

SELECT COUNT(*) FROM startups;

SELECT SUM(valuation) FROM startups;

SELECT MAX(raised) FROM startups WHERE stage = 'Seed';

SELECT MIN(founded) FROM startups;

SELECT AVG(valuation) FROM startups;

SELECT category, ROUND(AVG(valuation), 2) AS 'Valuation' FROM startups GROUP BY category ORDER BY Valuation DESC;

SELECT category, COUNT(*) AS 'Count' FROM startups GROUP BY category HAVING Count > 3;

SELECT location, AVG(employees) AS "Ave_Employees" FROM startups GROUP BY 1 HAVING Ave_Employees > 500 ORDER BY 2 DESC;