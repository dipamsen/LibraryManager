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

CREATE TABLE patrons (
    id CHAR(8) NOT NULL PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    name VARCHAR(30) NOT NULL,
    subscription_date DATE NOT NULL,
    CONSTRAINT id_length CHECK (LENGTH(TRIM(id)) = 8),
    CONSTRAINT valid_email CHECK (email LIKE '%@%.%')
);

CREATE TABLE transactions (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    book_isbn VARCHAR(13) NOT NULL,
    patron_id CHAR(8) NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    returned BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (book_isbn) REFERENCES books(isbn) ON DELETE CASCADE,
    FOREIGN KEY (patron_id) REFERENCES patrons(id) ON DELETE CASCADE
);

------------------------------------------
-- SEEDING
------------------------------------------
INSERT INTO
    books (quantity, title, author, isbn, genre)
VALUES
    (
        3,
        "The Sun Also Rises",
        "Ernest Hemingway",
        "9780743297332",
        "Fiction"
    ),
    (
        5,
        "To Kill A Mockingbird",
        "Harper Lee",
        "9780099549482",
        "Fiction"
    ),
    (
        3,
        "Their Eyes Were Watching God",
        "Zora Neale Hurston",
        "9780060838676",
        "Fiction"
    ),
    (
        2,
        "Pride and Prejudice",
        "Jane Austen",
        "9780140430721",
        "Fiction"
    ),
    (
        6,
        "Harry Potter and the Sorcerer's Stone",
        "J.K. Rowling",
        "9780439362139",
        "Fiction"
    ),
    (
        3,
        "The Hobbit",
        "J.R.R. Tolkien",
        "9780007525508",
        "Fiction"
    );

INSERT INTO
    patrons (
        id,
        email,
        name,
        subscription_date
    )
VALUES
    (
        "PATRON01",
        "patron1@example.com",
        "John Doe",
        "2023-08-01"
    ),
    (
        "PATRON02",
        "patron2@example.com",
        "Jane Smith",
        "2023-08-02"
    ),
    (
        "PATRON03",
        "patron3@example.com",
        "Michael Johnson",
        "2023-08-03"
    ),
    (
        "PATRON04",
        "patron4@example.com",
        "Emily Brown",
        "2023-08-04"
    ),
    (
        "PATRON05",
        "patron5@example.com",
        "David Wilson",
        "2023-08-05"
    );

INSERT INTO
    transactions (
        book_isbn,
        patron_id,
        issue_date,
        due_date,
        return_date,
        returned
    )
VALUES
    (
        "9780743297332",
        "PATRON01",
        "2023-08-01",
        "2023-08-15",
        NULL,
        FALSE
    ),
    (
        "9780099549482",
        "PATRON02",
        "2023-08-02",
        "2023-08-16",
        "2023-08-14",
        TRUE
    ),
    (
        "9780060838676",
        "PATRON03",
        "2023-08-03",
        "2023-08-17",
        NULL,
        FALSE
    ),
    (
        "9780743297332",
        "PATRON04",
        "2023-08-04",
        "2023-08-18",
        "2023-08-16",
        TRUE
    ),
    (
        "9780099549482",
        "PATRON01",
        "2023-08-05",
        "2023-08-19",
        NULL,
        FALSE
    ),
    (
        "9780060838676",
        "PATRON02",
        "2023-08-06",
        "2023-08-20",
        NULL,
        FALSE
    );