-- Script that creates the MySQL user user_0d_1 with all privileges
-- Password is set to 'user_0d_1_pwd' and script does not fail if user exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
