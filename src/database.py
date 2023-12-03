import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(user="root", host="localhost", passwd="dipam2006", database="library")
cursor = db.cursor()
cursor.execute("USE library")

# Try to execute SQL command
def TrySQLCommand(query, values=None):
  cursor.execute(query, values)
  result = cursor.fetchall()
  if cursor.rowcount == 0:
    raise ValueError("No matching records found.")
  return result, [desc[0] for desc in cursor.description]

# check for valid ISBN number
def ValidateISBN(isbn):
  # Remove hyphens and spaces
  isbn = isbn.replace("-", "").replace(" ", "")

  # ISBN-10
  if len(isbn) == 10:
    if not isbn[:-1].isdigit():
      return False
    if isbn[-1].upper() == "X":
      isbn_sum = (sum(int(digit) * (i + 1) for i, digit in enumerate(isbn[:-1])) + 10)
    else:
      isbn_sum = sum(int(digit) * (i + 1) for i, digit in enumerate(isbn))
    return isbn if isbn_sum % 11 == 0 else False

  # ISBN-13
  elif len(isbn) == 13:
    if not isbn.isdigit():
      return False
    isbn_sum = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn))
    return isbn if isbn_sum % 10 == 0 else False

  return False

# Edit Books Table Functions
# Replace Books
def ReplaceBook(oISBN, nQuantity, nTITLE, nAUTHOR, nISBN, nGenre):
  if ValidateISBN(nISBN) == False:
    print("INVALID ISBN NUMBER!!")
    return 1
  try:
    deletebook = "DELETE FROM books WHERE ISBN= %s"
    cursor.execute(deletebook, (oISBN, ))
  except ValueError:
    db.rollback()
    return 1
  newbooks = "INSERT INTO books (quantity, title, author, isbn, genre) VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(newbooks, (nQuantity, nTITLE, nAUTHOR, nISBN, nGenre))
  db.commit()

# Add Books
def AddBook(nQuantity, nTITLE, nAUTHOR, nISBN, nGenre):
  vISBN = ValidateISBN(nISBN)
  if vISBN == False:
    print("INVALID ISBN NUMBER!!")
    return 1
  try:
    newbooks = "INSERT INTO books (quantity, title, author, isbn, genre) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(newbooks, (nQuantity, nTITLE, nAUTHOR, vISBN, nGenre))
    db.commit()
  except ValueError:
    db.rollback()
    return 1

# Remove Books
def RemoveBook(ISBN):
  vISBN = ValidateISBN(ISBN)
  if vISBN == False:
    print("INVALID ISBN NUMBER!!")
    return 1
  try:
    deletebook = "DELETE FROM books WHERE isbn= %s;"
    cursor.execute(deletebook, (vISBN, ))
    db.commit()
  except ValueError:
    print("ISBN number not found. Check and Try Again!")
    db.rollback()
    return 1

# Searching Books
# By ISBN
def SearchBookByISBN(ISBN):
  try:
    SearchBook = "SELECT * FROM books WHERE isbn= %s;"
    return TrySQLCommand(SearchBook, (ISBN, ))
  except ValueError:
    db.rollback()
    return 1

# By Author
def SearchBookByAuthor(Author):
  try:
    SearchBook = "SELECT * FROM books WHERE author LIKE %s"
    return TrySQLCommand(SearchBook, ("%" + Author + "%", ))
  except ValueError:
    db.rollback()
    return 1

# By Title
def SearchBookByTitle(Title):
  try:
    SearchBook = "SELECT * FROM books WHERE title LIKE %s"
    return TrySQLCommand(SearchBook, ("%" + Title + "%", ))
  except ValueError:
    db.rollback()
    return 1

# By Genre
def SearchBookByGenre(Genre):
  try:
    SearchBook = "SELECT * FROM books WHERE genre LIKE %s"
    return TrySQLCommand(SearchBook, (Genre, ))
  except ValueError:
    db.rollback()
    return 1

def EditBook(ISBN):
  Search, columns = SearchBookByISBN(ISBN)
  if Search == 1:
    return 1
  else:
    print(tabulate(Search, headers=columns, tablefmt="pretty"))
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
        vID = ValidateISBN(id)
        if ISBN != id and vID:
          query = "UPDATE books SET isbn=%s WHERE isbn=%s"
          cursor.execute(query, (vID, ISBN))
          db.commit()
        else:
          print("Failed to edit! Try again!")
          db.rollback()
          return 1
      elif option == 2:
        Author = input("ENTER THE NEW AUTHOR NAME OF THE BOOK : ")
        cursor.execute("UPDATE books SET author=%s WHERE isbn=%s", (Author, ISBN))
        db.commit()
      elif option == 3:
        Title = input("ENTER THE NEW TITLE OF BOOK : ")
        cursor.execute("UPDATE books SET title=%s WHERE isbn=%s", (Title, ISBN))
        db.commit()
      elif option == 4:
        quantity = input("ENTER THE QUANTITY OF BOOK AVAILABLE : ")
        query = "UPDATE books SET quantity= %s WHERE isbn=%s"
        cursor.execute(query, (quantity, ISBN))
        db.commit()
      elif option == 5:
        genre = input("ENTER THE NEW GENRE OF BOOK : ")
        query = "UPDATE books SET genre= %s WHERE isbn=%s"
        cursor.execute(query, (genre, ISBN))
        db.commit()
      elif option == 6:
        RemoveBook(ISBN)

# Issue Books to Patron and updating the return status
def IssueBook(ISBN, ID):
  if SearchBookByISBN(ISBN) == 1:
    print("ISBN number not found. Check and Try Again!")
    return 1
  if SearchPatronByID(ID) == 1:
    print("Patron ID not found. Check and Try Again!")
    return 1
  # check if patron has less than 3 unreturned books
  check1 = ("SELECT COUNT(*) FROM transactions WHERE patron_id = %s AND returned IS FALSE")
  cursor.execute(check1, (ID, ))
  if cursor.fetchone()[0] >= 3:
    print("PATRON HAS ALREADY ISSUED 3 BOOKS! \nPLEASE RETURN A BOOK AND TRY AGAIN!")
    return 1

  # check if patron currently has this book
  check2 = "SELECT * FROM transactions WHERE patron_id = %s AND book_isbn = %s AND returned IS FALSE"
  cursor.execute(check2, (ID, ISBN))
  cursor.fetchall()
  if cursor.rowcount > 0:
    print("PATRON HAS ALREADY ISSUED THIS BOOK!")
    return 1

  query = "UPDATE books SET quantity = quantity - 1 WHERE isbn = %s AND quantity >= 1"
  cursor.execute(query, (ISBN, ))
  if cursor.rowcount == 1:
    try:
      issue = "INSERT INTO transactions (book_isbn, patron_id, issue_date, due_date) VALUES (%s, %s, CURDATE(), DATE(CURDATE() + 7))"
      cursor.execute(issue, (ISBN, ID))
      db.commit()
      # print("Book issued successfully!")
    except:
      db.rollback()
      print("Book issue failed!")
      return 1
  else:
    db.rollback()
    print("BOOK ISSUE COULD NOT BE COMPLETED AS BOOK OUT OF STOCK! \nPLEASE CHOOSE ANOTHER BOOK AND TRY AGAIN!")
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
  cursor.execute(query, (ISBN, ))
  db.commit()

def AddPatron(ID, Email, Patron_Name, Subcription_Date):
  newpatron = ("INSERT INTO patrons (id, email, name, subscription_date) VALUES(%s,%s,%s,%s)")
  cursor.execute(newpatron, (ID, Email, Patron_Name, Subcription_Date))
  db.commit()

def RemovePatron(ID):
  try:
    deletepatron = "DELETE FROM patrons WHERE id= %s;"
    TrySQLCommand(deletepatron, (ID, ))
  except ValueError:
    db.rollback()
    return 1
  db.commit()

def EditPatron(ID):
  Search = SearchPatronByID(ID)
  if Search == 1:
    return 1
  else:
    print(tabulate(Search, headers=["ID", "Email", "Name", "Subscription Date"], tablefmt="pretty"))
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
          cursor.execute(query, (id, ID))
          db.commit()
        else:
          print("Failed to edit! Try again!")
          db.rollback()
          return 1
      elif option == 2:
        Email = input("ENTER THE NEW EMAIL OF PATRON : ")
        if "@" in Email and "." in Email:
          cursor.execute("UPDATE patron SET email= %s WHERE id= %s", (Email, ID))
          db.commit()
        else:
          print("Enter a VALID EMAIL and Try Again!")
          db.rollback()
          return 1
      elif option == 3:
        Name = input("ENTER THE NEW NAME OF PATRON : ")
        cursor.execute("UPDATE patrons SET name= %s WHERE id= %s", (Name, ID))
        db.commit()
      elif option == 4:
        query = "UPDATE patrons SET subscription_date=DATE(NOW()) WHERE id=%s"
        cursor.execute(query, (ID, ))
        db.commit()
      elif option == 5:
        RemovePatron(ID)

def SearchPatronByID(ID):
  try:
    SearchPatron = "SELECT * FROM patrons WHERE id= %s"
    return TrySQLCommand(SearchPatron, (ID, ))
  except ValueError:
    db.rollback()
    return 1

def SearchPatronByName(Patron_Name):
  try:
    SearchPatron = "SELECT * FROM patrons WHERE name LIKE %s"
    return TrySQLCommand(SearchPatron, ("%" + Patron_Name + "%", ))
  except ValueError:
    db.rollback()
    return 1

def ViewTransactions():
  query = """SELECT t.id AS "ID", b.title AS "Book", p.name AS "Issued By", t.issue_date AS "Issued On", t.due_date AS "Due On", IFNULL(t.return_date, "Not Returned") AS "Returned On" 
             FROM transactions t, books b, patrons p 
             WHERE t.book_isbn = b.isbn 
               AND t.patron_id = p.id 
             ORDER BY t.book_isbn, t.issue_date;"""
  cursor.execute(query)
  columns = [desc[0] for desc in cursor.description]
  data = cursor.fetchall()
  print(tabulate(data, headers=columns, tablefmt="pretty"))

def ViewTransactionsPending():
  query = """SELECT t.id "ID", b.title "Book", p.name "Issued By", t.issue_date "Issued On", 
                    t.due_date "Due On", IFNULL(t.return_date, "Not Returned") "Returned On" 
             FROM transactions t, books b, patrons p 
             WHERE t.book_isbn = b.isbn 
               AND t.patron_id = p.id 
               AND t.returned = FALSE 
             ORDER BY t.book_isbn, t.issue_date;"""
  cursor.execute(query)
  columns = [desc[0] for desc in cursor.description]
  data = cursor.fetchall()
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

def Query(query, values=None):
  cursor.execute(query, values)
  data = cursor.fetchall()
  return data, [desc[0] for desc in cursor.description]
