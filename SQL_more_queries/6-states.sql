-- Script that creates the database hbtn_0d_usa and the table states
-- Table states has columns: id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL
-- Create database and table only if they do not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
