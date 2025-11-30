-- Script that creates the table unique_id
-- Table has columns: id INT with default value 1 and UNIQUE constraint, name VARCHAR(256)
-- Create table only if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
