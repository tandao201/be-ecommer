CREATE database userservice;
CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'test123';
GRANT ALL ON userservice.* TO 'test_user'@'localhost';