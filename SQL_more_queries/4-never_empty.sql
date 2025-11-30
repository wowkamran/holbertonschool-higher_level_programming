-- Script that creates the table id_not_null
-- Table has columns: id INT with default value 1, name VARCHAR(256)
-- Create table only if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
