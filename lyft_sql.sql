/*Using SQL to analyse data from ride sharing company Lyft */

SELECT * FROM trips LIMIT 5;

SELECT * FROM riders LIMIT 5;

SELECT * FROM cars LIMIT 5;

SELECT * FROM trips LEFT JOIN riders ON trips.rider_id = riders.id;

SELECT * FROM trips JOIN cars ON trips.car_id = cars.id;

SELECT * FROM riders UNION SELECT * FROM riders2 LIMIT 2;

SELECT ROUND(AVG(cost), 2) FROM trips;

SELECT * FROM riders WHERE total_trips < 500;

SELECT COUNT(*) FROM cars where status = 'active';

SELECT * FROM cars ORDER BY trips_completed DESC LIMIT 2;