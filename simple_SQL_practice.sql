/* Show current datases, create a new database and then delete it */
SHOW DATABASES;
CREATE DATABASE MovieIndustry;
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS MovieIndustry;
DROP DATABASE MovieIndustry;
SHOW DATABASES;

/* Create a new table */
CREATE TABLE IF NOT EXISTS Actors(
    Id INT AUTO_INCREMENT,
    FirstName VARCHAR(20) NOT NULL,
    SecondName VARCHAR(20) NOT NULL,
    DoB DATE NOT NULL,
    Gender ENUM('Male', 'Female', 'Transgender') NOT NULL,
    MaritalStatus ENUM('Married', 'Divorced', 'Single', 'Unknown') DEFAULT 'Unknown',
    NetWorthInMillions DECIMAL NOT NULL,
    PRIMARY KEY(id)
);

/* Insert a new row into the table */
INSERT INTO Actors(
        FirstName,
        SecondName,
        DoB,
        Gender,
        MaritalStatus,
        NetWorthInMillions
    )
VALUES (
        'Brad',
        'Pitt',
        '1963-12-18',
        'Male',
        'Single',
        240.00
    );

/* Querying data */
SELECT * FROM Actors;

SELECT FirstName, SecondName, Gender FROM Actors;

SELECT NetWorthInMillions FROM Actors WHERE FirstName = 'Brad';

SELECT * FROM Actors WHERE FirstName LIKE 'JEN%';

/* Deleting data */
DELETE FROM Actors WHERE FirstName = 'Brad'

/* Update Data  */
UPDATE Actors MaritalStatus = 'Unknown'; 
