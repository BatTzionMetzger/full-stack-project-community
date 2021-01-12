-- create database community_db;

USE community_db; 

-- CREATE TABLE community(
--     id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name varchar(50) NOT NULL,
--     password varchar(50),
--     admin_mail varchar(50) NOT NULL,
--     img_path varchar(50)
-- );


-- CREATE TABLE user(
--     mail VARCHAR(50) NOT NULL PRIMARY KEY,
--     password varchar(50),
--     name VARCHAR(50),
--     community_id INT NOT NULL,
--     phone VARCHAR(50),

--     FOREIGN KEY(community_id) REFERENCES community(id)
-- );

CREATE TABLE item(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    description varchar(100),
    is_available boolean default 1,
    ordered_by_mail varchar(50) ,
    owners_mail varchar(50) NOT NULL,
    img_path varchar(50),
    
    FOREIGN KEY(owners_mail) REFERENCES user(mail),
    FOREIGN KEY(ordered_by_mail) REFERENCES user(mail)
);

-- drop TABLE item

