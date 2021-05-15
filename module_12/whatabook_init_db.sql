-- CREATING ADMIN USER
DROP USER IF EXISTS 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

  -- CREATING TABLES


DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;

CREATE TABLE store (
    store_id    INT           NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)  NOT NULL,
    PRIMARY KEY(store_id)
);
CREATE TABLE book (
    book_id    INT            NOT NULL    AUTO_INCREMENT,
    book_name  VARCHAR(200)   NOT NULL,
    details    VARCHAR(500)   NULL,
    author     VARCHAR(200)   NOT NULL,
    PRIMARY KEY(book_id)
);
CREATE TABLE user (
    user_id     INT           NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)   NOT NULL,
    last_name   VARCHAR(75)   NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE wishlist (
    wishlist_id INT           NOT NULL    AUTO_INCREMENT,
    user_id     INT           NOT NULL,
    book_id     INT           NOT NULL,
    PRIMARY KEY(wishlist_id),
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);


  -- FILLING TABLES WITH 1 STORE, 9 BOOKS, 3 USERS (1 WISHLIST BOOK EACH)
INSERT INTO store(locale)
    VALUES('10 190 cedar sage dr, garland, Tx 75040');

INSERT INTO book(book_name, author)
    VALUES('In search of lost time', 'Marcel Proust');
INSERT INTO book(book_name, author)
    VALUES('Ulysses', 'James Joyce');
INSERT INTO book(book_name, author)
    VALUES('Don Quixote', 'Miguel');
INSERT INTO book(book_name, author)
    VALUES('One hundred year of solitude', 'Gabriel');
INSERT INTO book(book_name, author)
    VALUES('The great Gatsby', 'Scott');
INSERT INTO book(book_name, author)
    VALUES('Moby Dick', 'Herman');
INSERT INTO book(book_name, author)
    VALUES('War and peace', 'Leo');
INSERT INTO book(book_name, author)
    VALUES('Hamlet', 'shakespeare');
INSERT INTO book(book_name, author)
    VALUES('The Odyssey', 'Homer');

INSERT INTO user(first_name, last_name) 
    VALUES('Jon', 'Cena');
INSERT INTO user(first_name, last_name)
    VALUES('Peter', 'Parker');
INSERT INTO user(first_name, last_name)
    VALUES('Don', 'Jon');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jon'), 
        (SELECT book_id FROM book WHERE book_name = 'Moby Dick')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Peter'),
        (SELECT book_id FROM book WHERE book_name = 'The great Gatsby')
    );
INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Don'),
        (SELECT book_id FROM book WHERE book_name = 'Hamlet')
    );
