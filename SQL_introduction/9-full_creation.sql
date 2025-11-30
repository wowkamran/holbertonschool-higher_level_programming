-- Script that creates a table called second_table and inserts multiple rows
-- Table has columns: id INT, name VARCHAR(256), score INT
-- Create table only if it does not already exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
