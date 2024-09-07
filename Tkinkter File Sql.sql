-- Create the database
CREATE DATABASE registration;

-- Use the database
USE registration;

-- Create the registration_details table
CREATE TABLE IF NOT EXISTS registration_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(255),
    mobile VARCHAR(15)
);

-- Create a new MySQL user (replace 'your_username' and 'your_password' with your preferred credentials)
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';

-- Grant all privileges on the registration database to the new user
GRANT ALL PRIVILEGES ON registration.* TO 'your_username'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
