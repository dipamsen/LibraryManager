import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(
    user="root", host="localhost", passwd="dipam2006", database="library"
)
cursor = db.cursor()
cursor.execute("USE library")


# Try to execute SQL command
def TrySQLCommand(query, values=None):
    cursor.execute(query, values)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        raise ValueError("No matching records found.")
    return result


# check for valid ISBN number
def ValidateISBN(isbn):
    # Remove hyphens and spaces
    isbn = isbn.replace("-", "").replace(" ", "")

    # ISBN-10
    if len(isbn) == 10:
        if not isbn[:-1].isdigit():
            return False
        if isbn[-1].upper() == "X":
            isbn_sum = (
                sum(int(digit) * (i + 1) for i, digit in enumerate(isbn[:-1])) + 10
            )
        else:
            isbn_sum = sum(int(digit) * (i + 1) for i, digit in enumerate(isbn))
        return isbn_sum % 11 == 0

    # ISBN-13
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
        isbn_sum = sum(
            int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn)
        )
        return isbn_sum % 10 == 0

    return False


# Edit Books Table Functions
# Replace Books
def ReplaceBook(oISBN, nQuantity, nTITLE, nAUTHOR, nISBN, nGenre):
    if ValidateISBN(oISBN) == False:
        print("INVALID ISBN NUMBER!!")
        return 1
    try:
        deletebook = "DELETE FROM books WHERE ISBN= %s"
        TrySQLCommand(deletebook, (oISBN,))
    except ValueError:
        db.rollback()
        return 1
    newbooks = "INSERT INTO books (quantity, title, author, isbn, genre) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(newbooks, (nQuantity, nTITLE, nAUTHOR, nISBN, nGenre))
    db.commit()


# Add Books
def AddBook(nQuantity, nTITLE, nAUTHOR, nISBN, nGenre):
    newbooks = "INSERT INTO books(quantity, title, author, isbn, genre) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(newbooks, (nQuantity, nTITLE, nAUTHOR, nISBN, nGenre))
    db.commit()


# Remove Books
def RemoveBook(ISBN):
    if ValidateISBN(ISBN) == False:
        print("INVALID ISBN NUMBER!!")
        return 1
    try:
        deletebook = "DELETE FROM books WHERE isbn= %s;"
        TrySQLCommand(deletebook, (ISBN,))
    except ValueError:
        db.rollback()
        return 1
    db.commit()


# Searching Books
# By ISBN
def SearchBookByISBN(ISBN):
    if ValidateISBN(ISBN) == False:
        print("INVALID ISBN NUMBER!!")
        return 1
    try:
        SearchBook = "SELECT * FROM books WHERE isbn= %s;"
        return TrySQLCommand(SearchBook, (ISBN,))
    except ValueError:
        db.rollback()
        return 1


# By Author
def SearchBookByAuthor(Author):
    try:
        SearchBook = "SELECT * FROM books WHERE author LIKE %s"
        return TrySQLCommand(SearchBook, ("%" + Author + "%",))
    except ValueError:
        db.rollback()
        return 1


# By Title
def SearchBookByTitle(Title):
    try:
        SearchBook = "SELECT * FROM books WHERE title LIKE %s"
        return TrySQLCommand(SearchBook, ("%" + Title + "%",))
    except ValueError:
        db.rollback()
        return 1


genres = ["Fiction", "Non Fiction"]


# By Genre
def SearchBookByGenre(Genre):
    if Genre not in genres:
        print("INVALID GENRE!!")
        return 1
    try:
        SearchBook = "SELECT * FROM books WHERE genre LIKE %s"
        return TrySQLCommand(SearchBook, (Genre,))
    except ValueError:
        db.rollback()
        return 1


def EditBook(ISBN):
    if ValidateISBN(ISBN) == False:
        print("INVALID ISBN NUMBER!!")
        return 1
    Search = SearchBookByISBN(ISBN)
    if Search == 1:
        return 1
    else:
        print("OPTIONS : ")
        print("(1) ---> ISBN number")
        print("(2) ---> Book Author")
        print("(3) ---> Book Title")
        print("(4) ---> Quantity")
        print("(5) ---> Genre")
        print("(6) ---> Remove book")
        option = int(input("Enter OPTION NUMBER of what you want to edit : "))
        if option >= 1 and option <= 6:
            if option == 1:
                id = input("ENTER THE NEW ISBN NUMBER OF BOOK : ")
                if ISBN != id and ValidateISBN(id):
                    query = "UPDATE books SET isbn= %s WHERE isbn=%s"
                    cursor.execute(
                        query,
                        (
                            id,
                            ISBN,
                        ),
                    )
                    db.commit()
                else:
                    print("Failed to edit! Try again!")
                    db.rollback()
                    return 1
            elif option == 2:
                Author = input("ENTER THE NEW AUTHOR NAME OF THE BOOK : ")
                cursor.execute(
                    "UPDATE books SET author=%s WHERE isbn=%s",
                    (
                        Author,
                        ISBN,
                    ),
                )
                db.commit()
            elif option == 3:
                Title = input("ENTER THE NEW TITLE OF BOOK : ")
                cursor.execute(
                    "UPDATE books SET title=%s WHERE isbn=%s",
                    (
                        Title,
                        ISBN,
                    ),
                )
                db.commit()
            elif option == 4:
                quantity = input("ENTER THE QUANTITY OF BOOK AVAILABLE : ")
                query = "UPDATE books SET quantity= %s WHERE isbn=%s"
                cursor.execute(
                    query,
                    (
                        quantity,
                        ISBN,
                    ),
                )
                db.commit()
            elif option == 5:
                genre = input("ENTER THE NEW GENRE OF BOOK : ")
                query = "UPDATE books SET genre= %s WHERE isbn=%s"
                cursor.execute(
                    query,
                    (
                        genre,
                        ISBN,
                    ),
                )
                db.commit()
            elif option == 6:
                RemoveBook(ISBN)


# Issue Books to Patron and updating the return status
def IssueBook(ISBN, ID):
    if ValidateISBN(ISBN) == False:
        print("INVALID ISBN NUMBER!!")
        return 1
    if SearchBookByISBN(ISBN) == 1:
        print("ISBN number not found. Check and Try Again!")
        return 1
    if SearchPatronByID(ID) == 1:
        print("Patron ID not found. Check and Try Again!")
        return 1
    query = "UPDATE books SET quantity = quantity - 1 WHERE isbn = %s AND quantity >= 1"
    cursor.execute(query, (ISBN,))
    if cursor.rowcount == 1:
        db.commit()

        issue = "INSERT INTO transactions (book_isbn, patron_id, issue_date, return_date) VALUES (%s, %s, CURDATE(), DATE(CURDATE() + 7))"
        cursor.execute(issue, (ISBN, ID))
        db.commit()
        print("Book issued successfully!")
    else:
        db.rollback()
        print(
            "BOOK ISSUE COULD NOT BE COMPLETED AS BOOK OUT OF STOCK! \nPLEASE CHOOSE ANOTHER BOOK AND TRY AGAIN!"
        )
        return 1


def ReturnBook(ISBN, ID):
    if ValidateISBN(ISBN) == False:
        print("INVALID ISBN NUMBER!!")
        return 1
    if SearchBookByISBN(ISBN) == 1:
        print("ISBN number not found. Check and Try Again!")
        return 1
    if SearchPatronByID(ID) == 1:
        print("Patron ID not found. Check and Try Again!")
        return 1
    trans = "UPDATE transactions SET return_date = CURDATE(), returned = TRUE WHERE book_isbn = %s AND patron_id = %s AND return_date IS NULL AND returned = FALSE"
    cursor.execute(trans, (ISBN, ID))
    if cursor.rowcount == 0:
        print("No book issued to this patron with this ISBN number!")
        return 1

    db.commit()

    query = "UPDATE books SET quantity = quantity + 1 WHERE ISBN = %s"
    cursor.execute(query, (ISBN,))
    db.commit()

    print("Book returned successfully!")


def AddPatron(ID, Email, Patron_Name, Subcription_Date):
    newpatron = (
        "INSERT INTO patrons (id, email, name, subscription_date) VALUES(%s,%s,%s,%s)"
    )
    cursor.execute(
        newpatron,
        (
            ID,
            Email,
            Patron_Name,
            Subcription_Date,
        ),
    )
    db.commit()


def RemovePatron(ID):
    try:
        deletepatron = "DELETE FROM patrons WHERE id= %s;"
        TrySQLCommand(deletepatron, (ID,))
    except ValueError:
        db.rollback()
        return 1
    db.commit()


def EditPatron(ID):
    Search = SearchPatronByID(ID)
    if Search == 1:
        return 1
    else:
        print("OPTIONS : ")
        print("(1) ---> Patron ID number")
        print("(2) ---> Patron Email")
        print("(3) ---> Patron Name")
        print("(4) ---> Renew Patron Subcription Date")
        print("(5) ---> Remove Patron")
        option = int(input("Enter OPTION NUMBER of what you want to edit : "))
        if option >= 1 and option <= 5:
            if option == 1:
                id = input("ENTER THE NEW 8-DIGIT UNIQUE ID OF PATRON : ")
                if ID != id and len(id) == 8:
                    query = "UPDATE patron SET id= %s WHERE id=%s"
                    cursor.execute(
                        query,
                        (
                            id,
                            ID,
                        ),
                    )
                    db.commit()
                else:
                    print("Failed to edit! Try again!")
                    db.rollback()
                    return 1
            elif option == 2:
                Email = input("ENTER THE NEW EMAIL OF PATRON : ")
                if "@" in Email and "." in Email:
                    cursor.execute(
                        "UPDATE patron SET email= %s WHERE id= %s",
                        (
                            Email,
                            ID,
                        ),
                    )
                    db.commit()
                else:
                    print("Enter a VALID EMAIL and Try Again!")
                    db.rollback()
                    return 1
            elif option == 3:
                Name = input("ENTER THE NEW NAME OF PATRON : ")
                cursor.execute(
                    "UPDATE patrons SET name= %s WHERE id= %s",
                    (
                        Name,
                        ID,
                    ),
                )
                db.commit()
            elif option == 4:
                query = "UPDATE patrons SET subscription_date=DATE(NOW()) WHERE id=%s"
                cursor.execute(query, (ID,))
                db.commit()
            elif option == 5:
                RemovePatron(ID)


def SearchPatronByID(ID):
    try:
        SearchPatron = "SELECT * FROM patrons WHERE id= %s"
        return TrySQLCommand(SearchPatron, (ID,))
    except ValueError:
        db.rollback()
        return 1


def SearchPatronByName(Patron_Name):
    try:
        SearchPatron = "SELECT * FROM patrons WHERE name LIKE %s"
        return TrySQLCommand(SearchPatron, ("%" + Patron_Name + "%",))
    except ValueError:
        db.rollback()
        return 1


def ViewTransactions():
    query = "SELECT * FROM transactions"
    cursor.execute(query)
    # Fetch column names
    columns = [desc[0] for desc in cursor.description]
    # Fetch data
    data = cursor.fetchall()
    # Print tabulated data
    print(tabulate(data, headers=columns, tablefmt="pretty"))


def ViewPatrons():
    query = """SELECT patrons.id "ID", name "Name", email "Email ID", subscription_date "Subscribed on", COUNT(transactions.id) "Unreturned Books" 
FROM patrons 
LEFT JOIN transactions ON patrons.id = transactions.patron_id AND transactions.returned = false 
GROUP BY patrons.id, email, name, subscription_date;"""
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    print(tabulate(data, headers=columns, tablefmt="pretty"))


def ViewBooks():
    query = "SELECT * FROM books"
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    print(tabulate(data, headers=columns, tablefmt="pretty"))
