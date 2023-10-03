import mysql.connector
from tabulate import tabulate

BORROWING_PERIOD = 14 # days

db = mysql.connector.connect(
    user="root", host="localhost", passwd="dipam2006", database="library"
)
cursor = db.cursor()
cursor.execute("USE library")

def get_query(query, values=None):
    cursor.execute(query, values)
    columns = [column[0] for column in cursor.description]
    return cursor.fetchall(), columns

def update_query(query, values=None):
    cursor.execute(query, values)
    if cursor.rowcount == 0:
        raise Exception("No rows updated!")
    db.commit()

def issue_book(book_isbn, patron_id):
    # check if patron has <3 unreturned books
    check1 = get_query("SELECT COUNT(*) FROM transactions WHERE patron_id = %s AND returned IS FALSE", (patron_id,))[0]
    if check1[0][0] >= 3:
        raise Exception("Patron has already issued 3 books!")
    # check if patron has this book
    check2 = get_query("SELECT COUNT(*) FROM transactions WHERE patron_id = %s AND book_isbn = %s AND returned IS FALSE", (patron_id, book_isbn))[0]
    if check2[0][0] >= 1:
        raise Exception("Patron has already issued this book!")
    update_query(f"INSERT INTO transactions (book_isbn, patron_id, issue_date, due_date) VALUES (%s, %s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL {BORROWING_PERIOD} DAY))", (book_isbn, patron_id))
    try: 
        update_query("UPDATE books SET quantity = quantity - 1 WHERE id = %s AND quantity >= 1", (book_isbn,))
    except:
        update_query("DELETE FROM transactions WHERE book_isbn = %s AND patron_id = %s AND returned IS FALSE", (book_isbn, patron_id))
        raise Exception("Book not available!")



def show_table(table, columns=None):
    print(tabulate(table, headers=columns, tablefmt="rounded_outline"))

show_table(*get_query("SELECT * FROM patrons"))