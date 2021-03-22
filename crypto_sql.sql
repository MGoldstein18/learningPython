/* Analyzing transactions of a fictional crypto exchange using sql */

SELECT * FROM transactions LIMIT 5;

SELECT SUM(money_in) FROM transactions;

SELECT SUM(money_out) FROM transactions;

SELECT COUNT(money_in) FROM transactions;

SELECT COUNT(money_in) FROM transactions WHERE currency = 'BIT';

SELECT MAX(money_in) FROM transactions;

SELECT MAX(money_out) FROM transactions;

SELECT AVG(money_in) FROM transactions WHERE currency = 'ETH';

SELECT date AS 'Date', ROUND(AVG(money_in), 2) AS 'Average Buy', ROUND(AVG(money_out), 2) AS 'Average Sell' FROM transactions GROUP BY date;