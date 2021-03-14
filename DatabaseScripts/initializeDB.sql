-- Drop database from postgres if it exists (ensures that we get a clean dataset AFTER INITIAL RUN PROBABLY DON'T NEED TO DO THIS AGAIN)
DROP DATABASE IF EXISTS repeatermap;
--create the database instance in postgres
CREATE DATABASE repeatermap;
-- connect to the newly created database
\c repeatermap

--Table creation
CREATE TABLE IF NOT EXISTS test(
    id integer,
    testName varchar(30),
    PRIMARY KEY (id)
);

--data insertion, may occur elsewhere
INSERT INTO test(id,testName) VALUES (0, 'someTest');

--test to ensure that data was entered into the given database
SELECT COUNT(*) FROM test;