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
-- drop TABLE  item
-- CREATE TABLE item(
--     id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(50),
--     description varchar(100),
--     is_available boolean default 1,
--     ordered_by_mail varchar(50) ,
--     owners_mail varchar(50) NOT NULL,
--     img_path varchar(100),
    
--     FOREIGN KEY(owners_mail) REFERENCES user(mail),
--     FOREIGN KEY(ordered_by_mail) REFERENCES user(mail)
-- );

-- drop TABLE item

-- UPDATE item 
-- SET is_available = 1, ordered_by_mail = null;

-- select * from item;
-- select * from community;
-- select * from user;
-- use community_db;

-- DELETE from item;

-- DELETE from user;

-- DELETE from community;

-- INSERT INTO community (name, password, admin_mail, img_path) 
--     VALUES('Bnot Sara', 'Bnot Sara', 'metzgerbattzion@gmail.com', 'im1.PNG');

-- INSERT INTO community (name, password, admin_mail, img_path) 
--     VALUES('Beer Miriam', 'Beer Miriam', 'hadasdasdus@gmail.com', 'im2.PNG');

INSERT INTO user
        VALUES('hadasdasdus@gmail.com', '1234', 'Hadas1', 277, '0522345234');

INSERT INTO user
        VALUES('metzgerbattzion@gmail.com', '1234', 'BatTzion1', 277, '0528888888');

INSERT INTO user
        VALUES('saramor325@gmail.com', '1234', 'Sara1', 277, '0523333333');

INSERT INTO user
        VALUES('hadas.schacham@mail.huji.ac.il', '1234', 'Hadas2', 277, '0522345234');

INSERT INTO user
        VALUES('hhh@gmail.com', '1234', 'Hadas3', 278, '0522345234');

INSERT INTO user
        VALUES('hhh1@gmail.com', '1234', 'Sara3', 278, '0522345234');

INSERT INTO user
        VALUES('hhh2@gmail.com', '1234', 'BatTzion3', 278, '0522345234');


INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('chair', 'beautiful vintage chair', 'im1.PNG', 'metzgerbattzion@gmail.com');


INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('dress', 'beautiful vintage chair', 'im2.PNG', 'hadasdasdus@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('table', 'old rusty table', 'im3.PNG', 'saramor325@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('vase', 'antique vase', 'im4.PNG', 'metzgerbattzion@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('hat', 'cute pink hat', 'im5.PNG', 'metzgerbattzion@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('menora', 'brass menora', 'im6.PNG', 'metzgerbattzion@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('doll', 'will give your child great joy', 'im7.PNG', 'metzgerbattzion@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('scarf', 'beautiful scarf', 'im8.PNG', 'hadasdasdus@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('hat', 'winter hat', 'im9.PNG', 'hadasdasdus@gmail.com');

INSERT INTO item (name, description, img_path, owners_mail)
    VALUES('bowl', 'coconut bowl', 'im10.PNG', 'hadasdasdus@gmail.com');

-- SELECT * from item;