#Task 1
SELECT *
FROM transaction_data
LIMIT 10;

SELECT full_name, email 
FROM transaction_data
WHERE zip = 20252;

SELECT full_name, email 
FROM transaction_data
WHERE full_name = 'Art Vandelay' OR full_name LIKE '% der %';

SELECT ip_address, email
FROM transaction_data
WHERE ip_address LIKE '10.%';

SELECT email
FROM transaction_data 
WHERE email LIKE '%temp_email.com';


SELECT * 
FROM transaction_data
WHERE full_name LIKE 'John%' AND ip_address LIKE '120.%'


#Task 2
SELECT *
FROM users
LIMIT 20;
 
SELECT email, birthday
FROM users
WHERE birthday BETWEEN '1980-01-01' AND '1989-12-31';
   
SELECT email, created_at 
FROM users
WHERE created_at < '2017-05-01';

SELECT email
FROM users
WHERE test = 'bears';

SELECT email
FROM users
WHERE campaign LIKE 'BBB-_';

SELECT email
FROM users
WHERE campaign LIKE '%2';


SELECT email 
FROM users
WHERE campaign IS NOT NULL and test IS NOT NULL;