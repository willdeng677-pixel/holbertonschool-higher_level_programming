CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO states (id, name) VALUES
(1, 'California'),
(2, 'Arizona'),
(3, 'Texas'),
(4, 'New York'),
(5, 'Nevada');
