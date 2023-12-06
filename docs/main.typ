#import "template.typ": *
#import "code.typ": codes, screenshots
#import "@preview/sourcerer:0.2.1": code


#show: project.with(
  title: "Project Report on Software for Library Management",
  authors: ("Arghya Kumar", "Dipam Sen", "Maanya Kansara"),
  date: "2023",
)

#let code = code.with(number-align: right, line-offset: 10pt, line-spacing: 0.65em)

= Introduction

// The Library Manager is designed to facilitate the process of book issuance and returns in a library environment. This application offers a solution for tracking transactions, simplifying administrative tasks, and presenting data in a clear manner. Users can efficiently manage the database by updating, creating, and removing records. The goal is to make the application mor accessible by streamlining library operations and transaction management.

This application aims to solve the problem of efficient management of library
records. It offers a solution for tracking transactions, and managing data about
books and patrons in an organised way. The user can efficiently manage the
database by creating, updating and removing records. The goal is to facilitate
library operations by using technology to manage them conveniently.

The *Library Manager* Application is a command line application (CLI) which allows users to perform certain library operations. The application can be accessed by both the Admin and the Patrons (users/members) of the library.

Users login to the application by providing their respective password (admin) or ID (patron), upon which a list of functions are presented. Users can select their desired function by entering the corresponding number. The application then prompts the user for the necessary inputs, and executes the function. The output is then displayed to the user.

The library administrator can add, update or remove book records, and also update patron information. Furthermore, the admin can issue and return books, as well as view all transactions, with due dates and return status.

The patron can view all books, search for books, and view their own transactions. They can also issue and return books, and view their pending transactions.

#pagebreak(weak: true)

= Benefits and Limitations

#v(1cm)

*Benefits*
- Efficient management of library records

- Simple interface for interacting with the database

- Error-prone and secure
#v(1cm)

*Limitations*
- Tedious to use due to menu based CLI - more suitable for a GUI or web app

- Lack of networking

- Limited functionality 

#v(1cm)
*Scope of Improvement*
- SQL Server can be hosted on a server machine, allowing for Client-Server networking and accessibility.

- Third party modules like `inquirer` can be used to create better CLI interfaces rather than implementing a menu based interface.

- A GUI or web app can be created to make the application more user friendly and accessible.

#pagebreak(weak: true)

= Technologies Used

This project uses Python as the primary programming language for the frontend
application. The project uses an MySQL database for the backend, for efficient
data storage and retrieval.


*Hardware:*
- X86 64-bit processor
- 4GB RAM

*Software:*
- Operating System: Windows 10
- Python 3.12
- MySQL Server 8.0



= Functional Requirements

The following are the functional requirements for a library management system:

*Admin Functions*

- To list and search books by criteria
- To add, remove and update books
- To view information about patrons
- To issue books and return books
- To view all transactions

*Patron Functions*
- To list and search books by criteria
- To issue books and return books
- To view self transactions (completed and pending)



#pagebreak(weak: true)


#let Books = field(`Books`, col: orange.darken(20%))
#let Patrons = field(`Patrons`, col: red.darken(0%))
#let Transactions = field(`Transactions`)


#let Book = field(`Book`, col: orange.darken(20%))
#let Patron = field(`Patron`, col: red.darken(0%))
#let Transaction = field(`Transaction`)

= Database Design
// #image("image.png")

The database for our application is managed by a SQL Database. It comprises of 3
tables: #Books, #Patrons, and #Transactions. The ERD (Entity Relationship
Diagram) shows the various relations and fields in the database (Figure 1).


#place(
  bottom,
  float: true,
  figure(image("diagram.png"), caption: "Database Entity Relationship diagram"),
)

== `Books`

The #Books table stores information on books, storing `isbn`, `title`, `author`,
`quantity` and `genre`.

- `isbn`: The International Standard Book Number uniquely identifying each book.
  (Primary Key)
- `title`: The title of the book.
- `author`: The author of the book.
- `quantity`: The number of available copies of the book.
- `genre`: The genre of the book.


== `Patrons`

The #Patrons table stores user info, about library patrons who can borrow and
return books.

- `id`: A unique identifier for each patron. (Primary Key)
- `email`: The email address of the patron.
- `name`: The name of the patron.
- `subscription_date`: The date when the patron subscribed to the library.


== `Transactions`

The #Transactions table keeps track of all issuings, with their date of issue
and date of return. It helps manage the circulation of books, tracking their
status and due dates, and allowing for reporting and analysis.

- `id`: A unique identifier for each transaction. (Primary Key)
- `book_isbn`: A foreign key referencing the "books" table, specifying the ISBN of
  the book involved.
- `patron_id`: A foreign key referencing the "patrons" table, identifying the
  patron associated.
- `issue_date`: The date when the book was issued.
- `due_date`: The date when the book is expected to be returned.
- `return_date`: The date when the book was actually returned (if returned).
- `returned`: A boolean indicating whether the book has been returned (default is
  false).

The database schema is defined in the #link(<db-sql>, field(strong(`db.sql`), col: black)) file.

#pagebreak(weak: true)


= Functional Decomposition

The application is decomposed into smaller components, which include:
- functionality for querying the database
- the main program (driver)

All database queries are isolated inside a separate file, #link(<database-py>, field(strong(`database.py`), col: black)).

#figure(code[```py
        # database.py
        
        def IssueBook(isbn, patron_id):
          ...
        
        def ReturnBook(isbn, patron_id):
          ...
        
        def ViewTransactions():
          ...
        
        ...
        
        ```], caption: "Function decomposition of database functions")

These functions use the `mysql.connecter` library to connect to the MySQL
database and query the database, and also return output and report errors
wherever applicable. 

The main frontend code is present inside #link(<main-py>, field(strong(`main.py`), col: black)),
which creates a menu based UI (within the terminal) for interacting with these
database functions.

#figure(code[```py
        # main.py
        
        print("Welcome to the Library Manager!!")
        print("(1) ADMIN")
        print("(2) USER")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
          # admin
          input("Enter password")
          ...
        elif choice == 2:
          # patron
          input("Enter patron ID")
          ...
        
          ```], caption: "Frontend code for interacting with the database")

Inside each conditional, the menu options are listed, and the user is prompted
for their choice. At the innermost level, the database functions are called, and
the output is shown.

#figure(code[```py
        # main.py
        
        while True: 
          opt = int(input("\tEnter your choice: "))
          ...
          elif opt == 5: # return book
            ISBN = input("\t\tISBN : ")
            ID = input("\t\tID of the patron: ")
            db.ReturnBook(ISBN, ID)
            print("\t\tBook returned successfully!")
        
          ```], caption: "Calling database functions in the frontend")
// #figure(sourcecode()[
//   ```py
// # main.py
// actions = [
//     {
//         "text": "Issue Books", 
//         "value": db.IssueBook
//     },
//     {
//         "text": "Return Books", 
//         "value": db.ReturnBook
//     },
//     {
//         "text": "View Transactions", 
//         "value": db.ViewTransactions
//     },
//     ...
// ]
//   ```
// ], caption: "Mapping menu options to database functions")

// During runtime, the program continuously presents the user with the menu choices, and upon selection, it uses the *`inspect`* module to determine the parameters required by the chosen function. It then dynamically prompts the user for the necessary input, eliminating the need for repetitive code for user input handling. 

// For example, in case of the `ReturnBook` function, the *`inspect.getfullargspec`* can determine its parameters - `isbn` and `patron_id`. Using this, the driver code can dynamically create user inputs requesting for these values, and then call the function, showing the output.

// #figure(sourcecode[
//   ```py
//   # main.py
//   choice = {"text": "Return Books", "value": db.ReturnBook} # choice selected by the user

//   # the function to execute
//   func = choice["value"] 

//   # gets list of arguments to the function
//   # ["isbn", "patron_id"]
//   args = inspect.getfullargspec(func).args 

//   params = []
//   for arg in args:
//     params.append(input(f"Enter {arg}: "))

//   # call the function with the provided arguments
//   func(*params)
 
//   ```
// ], caption: "Dynamically determining function parameters")

// This strategy offers a flexible and organized way to interact with various admin functions while maintaining clarity and reducing the overall complexity of the driver code.

#pagebreak()

= Control Flow of the Application

Upon launching the app, two options are presented: utilizing the application as
an admin or as a user (patron). The primary functionalities of the app are
exclusively accessible to the admin, for evident reasons. On the other hand, the
user is limited to performing a few read operations.

The admin operations are:

- Add/Remove/Edit a Book
- Add/Remove/Edit a Patron
- View Books/Patrons
- Search Books
- Issue/Return a Book
- View all Transactions
- View pending Transactions

Most of these functions just perform simple CRUD #footnote[Create, Read, Update, Delete] operations
using SQL queries and return the output (if any). The custom functionality which
is implemented specifically for this project is the Issue/Return workflow, which
is defined based on its *constraints* and *actions.*

== Issuing a Book

The `IssueBook()` function takes in two arguments - `isbn` and `patron_id`. The
steps of the Issue workflow are:

- Constraints
  + `isbn` must link to a specific #Book
  + `patron_id` must link to a specific #Patron
  + #Patron must not currently have 3 unreturned books
  + #Patron must not currently have this book
- Actions
  + Update `quantity` of #Book to `quantity - 1`
  + Create a #Transaction linking the #Patron and the #Book, with the current date
    as `issue_date`, and with a 7 day time interval, a `return_date`.
  + Commit to the Database.

== Returning a Book

Similar to the Issue Book workflow, the `ReturnBook()` function also takes in
arguments - `isbn` and `patron_id`.


- Constraints
  + `isbn` must link to a specific #Book
  + `patron_id` must link to a specific #Patron
  + #Patron must currently have this book - i.e. There should be one #Transaction such
    that it is associated with this #Patron and this #Book, and has `returned` set
    to `FALSE`.
- Actions
  + Update `returned = TRUE` and `return_date` to current date of #Transaction.
  + Update `quantity` of #Book to `quantity + 1`
  + Commit to the Database.



#pagebreak(weak: true)

= Modules Used

#[
  #set heading(outlined: false)


The following modules are used in the application:

== *`mysql.connector`*

MySQL Connector/Python is a standardized database driver for Python platforms, used to connect to the MySQL database and execute queries.

- `connector.connect()`: Connects to the MySQL database using the specified credentials.
- `connector.cursor()`: Creates a cursor object, which is used to execute queries.
- `cursor.execute()`: Executes the specified SQL query.
- `cursor.fetchall()`: Returns all rows of a query result.
- `cursor.commit()`: Commits the changes to the database.

== *`tabulate`*

Tabulate is a Python library used for printing tabular data in the terminal.

- `tabulate()`: Prints the specified data in a tabular format.

== *`tkinter.simpledialog`*

Used for creating simple modal dialogs for user input.

- `simpledialog.askstring()`: Creates a dialog box with a text field, and returns the input.

]

#pagebreak(weak: true)

#[
#set par(justify: false)

= User Defined Functions
#set text(0.95em)

In #link(<database-py>, field(strong(`database.py`), col: black)), different functions for performing database operations are defined.
- `AddBook()`: Adds a new book to the database.
- `RemoveBook()`: Removes a book from the database.
- `SearchBookByISBN()`, `SearchBookByTitle()`, `SearchBookByAuthor()`, `SearchBookByGenre()`: Searches for a book by the specified criteria.
- `EditBook()`: Edits the details of a book. (quantity)
- `IssueBook()`: Issues a book to a patron.
- `ReturnBook()`: Returns a book from a patron.
- `AddPatron()`: Adds a new patron to the database.
- `RemovePatron()`: Removes a patron from the database.
- `EditPatron()`: Edits the details of a patron.
- `SearchPatronByID()`, `SearchPatronByName()`: Searches for a patron by the specified criteria.
- `ViewTransactions()`: Views all transactions.
- `ViewPendingTransactions()`: Views all pending transactions.
- `ViewBooks()`: Views all books.
- `ViewPatrons()`: Views all patrons.

Additionally, there are some helper functions for common tasks to avoid code repetition.

- `ValidateISBN()`: Checks if the given ISBN is valid by using check digits.
- `ValidateDate()`: Checks if the given date is in valid format.
- `TrySQLCommand()` : Executes the given SQL command and returns the output along with column headers.
- `showtable()`: Displays the given data in a tabular format.
- `triminput()`: Takes user input and removes leading and trailing whitespaces.
- `numinput()`: Takes valid numerical input from the user.

]

#pagebreak(weak: true)


= Source Code

// The complete source code for the application as well as this document is accessible on the GitHub repository for the project:
// https://github.com/dipamsen/LibraryManager

#codes

#pagebreak(weak: true)

= Output

#screenshots

// #read("screenshots/*")


#pagebreak(weak: true)

#bigheading("Bibliography", outlined: true)

#bibliography("works.yml", title: none, full: true, style: "ieee")