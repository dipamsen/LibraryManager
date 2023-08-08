DROP DATABASE IF EXISTS library;

CREATE DATABASE library;

USE library;

CREATE TABLE books (
    isbn VARCHAR(13) NOT NULL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    genre ENUM("Fiction", "Non-Fiction") NOT NULL
);

INSERT INTO
    books (quantity, title, author, isbn)
VALUES
    (
        3,
        "The Sun Also Rises",
        "Ernest Hemingway",
        "9780743297332"
    ),
    (
        2,
        "To Kill A Mockingbird",
        "Harper Lee",
        "9780099549482"
    ),
    (
        2,
        "Their Eyes Were Watching God",
        "Zora Neale Hurston",
        "9780060838676"
    );

CREATE TABLE patrons (
    id CHAR(8) NOT NULL PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    name VARCHAR(30) NOT NULL,
    subscription_date DATE NOT NULL,
    return_status BOOL NOT NULL DEFAULT TRUE,
    CONSTRAINT id_length CHECK (LENGTH(TRIM(id)) = 8),
    CONSTRAINT valid_email CHECK (email LIKE '%@%.%')
);

CREATE TABLE issues (
    id INT NOT NULL PRIMARY KEY,
    book_isbn VARCHAR(13) NOT NULL,
    patron_id CHAR(8) NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE NOT NULL,
    -- returned BOOL NOT NULL DEFAULT FALSE,
    FOREIGN KEY (book_isbn) REFERENCES books(isbn) ON DELETE CASCADE,
    FOREIGN KEY (patron_id) REFERENCES patrons(id) ON DELETE CASCADE
);