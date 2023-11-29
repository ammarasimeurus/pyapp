CREATE DATABASE IF NOT EXISTS responses;

-- Check if the user 'pyapp'@'localhost' exists before creating
CREATE USER IF NOT EXISTS 'pyapp'@'%' IDENTIFIED BY '123_abcde';

-- Grant privileges only if the user was just created or does not have them
GRANT ALL PRIVILEGES ON responses.* TO 'pyapp'@'%' WITH GRANT OPTION;

-- Make sure privileges take effect
FLUSH PRIVILEGES;

use responses;

CREATE TABLE IF NOT EXISTS url_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    status_code INT NOT NULL
);
