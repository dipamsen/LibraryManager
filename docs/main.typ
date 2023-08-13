#import "template.typ": *
#import "code.typ": code
#import "@preview/codelst:1.0.0": sourcecode


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


= Technologies Used

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

The database for our application is managed by MySQL - it comprises of 3 tables: #Books, #Patrons, and #Transactions. The ERD (Entity Relationship Diagram) shows the various relations and fields in the database (See Figure 1).

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

The #Transactions table keeps track of all issuings, with their date of issue and date of return. It helps manage the circulation of books, tracking their status and due dates, and allowing for reporting and analysis.

- `id`: A unique identifier for each transaction.
- `book_isbn`: A foreign key referencing the "books" table, specifying the ISBN of the book involved.
- `patron_id`: A foreign key referencing the "patrons" table, identifying the patron associated.
- `issue_date`: The date when the book was issued.
- `due_date`: The date when the book is expected to be returned.
- `return_date`: The date when the book was actually returned (if returned).
- `returned`: A boolean indicating whether the book has been returned (default is false).

#pagebreak(weak: true)


= Functional Decomposition

The application is decomposed into smaller components, which include:
- functionality for querying the database
- general utility functions
- the main program (driver)

All database queries are isolated inside a separate file, #link(<database-py>, field(strong(`database.py`), col: black)).

#figure(sourcecode[```py
# database.py

def IssueBook(isbn, patron_id):
  ...

def ReturnBook(isbn, patron_id):
  ...

def ViewTransactions():
  ...

...

```], caption: "Function decomposition of database functions")

These functions use the `mysql.connecter` library to connect to the MySQL database and query the database.

The main driver code is present inside main.py, which uses an interesting strategy to dynamically manage the menu-based interface for admin functions. Instead of hardcoding separate sections for each menu option, the code defines a list containing the display text of the option and its corresponding function. 

#figure(sourcecode()[
  ```py
# main.py
actions = [
    {
        "text": "Issue Books", 
        "value": db.IssueBook
    },
    {
        "text": "Return Books", 
        "value": db.ReturnBook
    },
    {
        "text": "View Transactions", 
        "value": db.ViewTransactions
    },
    ...
]
  ```
], caption: "Mapping menu options to database functions")

During runtime, the program continuously presents the user with the menu choices, and upon selection, it uses the *`inspect`* module to determine the parameters required by the chosen function. It then dynamically prompts the user for the necessary input, eliminating the need for repetitive code for user input handling. 

For example, in case of the `ReturnBook` function, the *`inspect.getfullargspec`* can determine its parameters - `isbn` and `patron_id`. Using this, the driver code can dynamically create user inputs requesting for these values, and then call the function, showing the output.

#figure(sourcecode[
  ```py
  # main.py
  choice = {"text": "Return Books", "value": db.ReturnBook} # choice selected by the user

  # the function to execute
  func = choice["value"] 

  # gets list of arguments to the function
  # ["isbn", "patron_id"]
  args = inspect.getfullargspec(func).args 

  params = []
  for arg in args:
    params.append(input(f"Enter {arg}: "))

  # call the function with the provided arguments
  func(*params)
  
  ```
], caption: "Dynamically determining function parameters")


This strategy offers a flexible and organized way to interact with various admin functions while maintaining clarity and reducing the overall complexity of the driver code.


= Control Flow of the Application

Initially on running the app, it provides with two options #sym.dash.em to use the application as an *Admin* or an *User* (Patron). The major functionality of an app is only accessible to the admin for obvious reasons, and the user can only perform a few READ operations.

The admin operations are:

- Add/Remove/Edit a Book
- Add/Remove/Edit a Patron
- View Books/Patrons
- Search Books
- Issue/Return a Book
- View all Transactions
- View pending Transactions

Most of these functions just perform simple CRUD SQL queries and return the output (if any). The custom functionality which is implemented specifically for this project is the Issue/Return workflow.

== Issuing a Book

The `IssueBook()` function takes in two arguments - `isbn` and `patron_id`. The following database commands take place:
// 1. Check if 


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