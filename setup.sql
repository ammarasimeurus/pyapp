CREATE DATABASE responses;
CREATE USER 'pyapp'@'localhost' IDENTIFIED BY '123_abcde';
GRANT ALL PRIVILEGES ON responses.* TO 'pyapp'@'localhost';
FLUSH PRIVILEGES;
CREATE TABLE url_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    status_code INT NOT NULL
);
