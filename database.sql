CREATE DATABASE tinyurl;
USE tinyurl;

CREATE TABLE urls(
	ID int AUTO_INCREMENT,
    url varchar(60),
    encoded_url varchar(40),
    primary key(ID,url)
);
