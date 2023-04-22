CREATE DATABASE IF NOT EXISTS measurements_db;

USE measurements_db;

CREATE TABLE IF NOT EXISTS measurements (
    id INT(11) NOT NULL AUTO_INCREMENT,
    height FLOAT NOT NULL,
    weight FLOAT NOT NULL,
    age INT(11) NOT NULL,
    waist FLOAT NOT NULL,
    PRIMARY KEY (id)
);