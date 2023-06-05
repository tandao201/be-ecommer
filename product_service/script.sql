CREATE DATABASE  productservice;
CREATE USER 'product_user'@'localhost' IDENTIFIED BY 'test123';
GRANT ALL ON productservice.* TO 'product_user'@'localhost';