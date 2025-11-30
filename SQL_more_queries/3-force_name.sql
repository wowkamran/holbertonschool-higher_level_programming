-- Script that creates the table force_name
-- Table has columns: id INT, name VARCHAR(256) NOT NULL
-- Create table only if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
