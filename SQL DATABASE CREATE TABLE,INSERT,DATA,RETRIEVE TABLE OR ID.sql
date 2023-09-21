CREATE DATABASE users;
USE users;
 
-----CREATE TABLE-------
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role VARCHAR(255)
);
-------INSERT DATA----

INSERT INTO users (name, email, role) VALUES
    ('John Doe', 'john@example.com', 'Admin'),
    ('Jane Smith', 'jane@example.com', 'User');
	
	-- Retrieve all users from the "users" table
SELECT * FROM users;
-- Retrieve a specific user by their ID (e.g., ID=1)
SELECT * FROM users WHERE id = 1;