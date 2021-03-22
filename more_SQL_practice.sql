/* Below are SQL queries to three databases which belong to a fictional streaming company.
The users database contains user information, the watch_history contains information about 
each watching event and the payments database contains info about payments.  */


/* Query to get the single longest and shortest watching events */
SELECT MAX(watch_duration_in_minutes) AS 'max', MIN(watch_duration_in_minutes) AS 'min' FROM watch_history

/* Get the average amount for successful payments */
SELECT AVG(amount) FROM payments WHERE status = 'paid'

/* Get the total amount of money paid on each day and sort by amount of money */
SELECT pay_date, SUM(amount) AS 'amount' from payments WHERE status = 'paid' GROUP BY pay_date ORDER BY amount DESC

/* Get the total number of minutes streamed, rounded to nearest minute */
SELECT ROUND(SUM(watch_duration_in_minutes), 0) FROM watch_history

/* Get users and the number of minutes watched for users who watched more than 400 minutes */
SELECT user_id as 'User', SUM(watch_duration_in_minutes) as 'Total_Watch_Time' FROM watch_history GROUP BY 1 HAVING Total_Watch_Time > 400

/* Get the totoal amount paid per user who has made a successful payment */
SELECT user_id as 'User', SUM(amount) as 'Total' FROM payments WHERE status = 'paid' GROUP BY user_id ORDER BY Total DESC

/* Get distribution of watch events - ie: count how many time people watch for 1 minute, for 2 minutes, etc... */
SELECT ROUND(watch_duration_in_minutes, 0) AS 'duration', COUNT(*) AS 'count' FROM watch_history GROUP BY 1 ORDER BY 1

/* Find the most popular first names from the users */
SELECT first_name, COUNT(*) AS 'count' FROM users GROUP BY 1 ORDER BY 2 DESC

/* Find the number of users who have email addresses ending in '.com' */
SELECT COUNT(*) FROM users WHERE email LIKE '%.com'

