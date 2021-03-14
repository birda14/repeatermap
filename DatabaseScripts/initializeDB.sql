-- Drop database from postgres if it exists (ensures that we get a clean dataset AFTER INITIAL RUN PROBABLY DON'T NEED TO DO THIS AGAIN)
DROP DATABASE IF EXISTS repeatermap;
--create the database instance in postgres
CREATE DATABASE repeatermap;
-- connect to the newly created database
\c repeatermap

--Extend database to use postgis
CREATE EXTENSION postgis;

--test to ensure gis version is as expected
select postGIS_version();

--Drop all Tables
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS state;
DROP TABLE IF EXISTS repeater;

--Table creation
CREATE TABLE country(
    CountryID SERIAL,
    CountryName varchar(60),
    PRIMARY KEY(CountryID)
);

CREATE TABLE state(
    StateId varchar(10),
    StateName varchar(60),
    CountryID SERIAL,
    PRIMARY KEY(StateId),
    CONSTRAINT fk_country
        FOREIGN KEY(CountryID)
            REFERENCES country(CountryID)
);

CREATE TABLE repeater(
    RepeaterId integer,
    StateId varchar(10),
    PRIMARY KEY(RepeaterId),
    CONSTRAINT fk_state
        FOREIGN KEY(StateId)
            REFERENCES state(StateId)
);

\dt