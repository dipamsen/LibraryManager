#import "template.typ": *
#import "code.typ": code


#show: project.with(
  title: "Project Report on Software for Library Management",
  authors: (
    "Dipam Sen",
    "Arghya Kumar",
    "Manya Kansara"
  ),
  date: "2023",
)

= Introduction

The Library Manager is designed to facilitate the process of book issuance and returns in a library environment. This application offers a solution for tracking transactions, simplifying administrative tasks, and presenting data in a clear manner. Users can efficiently manage the database by updating, creating, and removing records. The goal is to make the application mor accessible by streamlining library operations and transaction management.


= Technologies used

This project uses Python as the primary programming language for the frontend application. The project uses an MySQL database for the backend, for efficient data storage and retrieval.


= Functional Requirements

The following are the functional requirements for a library management system:

- To list and search books by criteria
- To add, remove and update books
- To view information about patrons
- To issue books and return books
- To view and filter information about book issuance

#pagebreak(weak: true)


#let Books = field(`Books`)
#let Patrons = field(`Patrons`)
#let Transactions = field(`Transactions`)

= Database Design
// #image("image.png")

The database for our application is managed by MySQL - it comprises of 3 tables: #Books, #Patrons, and #Transactions. The ERD (Entity Relationship Diagram) shows the various relations and fields in the database.

== `Books`

The #Books table stores information on books, storing `isbn`, `title`, `author`, `quantity` and `genre`.

- `isbn`: The International Standard Book Number uniquely identifying each book.
- `title`: The title of the book.
- `author`: The author of the book.
- `quantity`: The number of available copies of the book.
- `genre`: The genre of the book.

#place(auto, float: true, figure(image("image.png"), caption: "Database Entity Relationship diagram"))

== `Patrons`

The #Patrons table stores user info, about library patrons who can borrow and return books.

- `id`: A unique identifier for each patron.
- `email`: The email address of the patron.
- `name`: The name of the patron.
- `subscription_date`: The date when the patron subscribed to the library.

== `Transactions`

The #Transactions table records interactions between patrons and books, including issuing and returning. It helps manage the circulation of books, tracking their status and due dates, and allowing for reporting and analysis.

- `id`: A unique identifier for each transaction.
- `book_isbn`: A foreign key referencing the "books" table, specifying the ISBN of the book involved.
- `patron_id`: A foreign key referencing the "patrons" table, identifying the patron associated.
- `issue_date`: The date when the book was issued.
- `due_date`: The date when the book is expected to be returned.
- `return_date`: The date when the book was actually returned (if returned).
- `returned`: A boolean indicating whether the book has been returned (default is false).

#pagebreak(weak: true)

= Control Flow of the Application

Initially on running the app, it provides with two options #sym.dash.em to use the application as an *Admin* or an *User* (Patron). The major functionality of an app is only accessible to the admin for obvious reasons, and the user can only perform READ operations.

The admin operations are:

- Add/Remove/Edit a Book
- Add/Remove/Edit a Patron
- View Books/Patrons
- Issue/Return a Book
- View all Transactions
- View pending Transactions



#pagebreak(weak: true)

= Source Code

// The complete source code for the application as well as this document is accessible on the GitHub repository for the project:
// https://github.com/dipamsen/LibraryManager

#code

#pagebreak(weak: true)

= Screenshots



#pagebreak(weak: true)


#let include-bib(key) = [
  #set text(0pt)
  #place(cite(key))
]

#for key in yaml("works.yml").keys() {
  include-bib(key)
}

#bigheading("Bibliography")

#bibliography("works.yml", title: none)