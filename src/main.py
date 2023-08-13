from tkinter import simpledialog
import time
import database as db
from tabulate import tabulate


def validate_date(date):
    # yyyy-mm-dd
    try:
        time.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def triminput(*args, **kwargs):
    return input(*args, **kwargs).strip()

def numinput(*args, **kwargs):
    while True:
        try:
            return int(input(*args, **kwargs))
        except ValueError:
            print("Invalid input! Please enter a number.")


print("Welcome to the Library Manager!!")
print()
print("ACCESS TO : ")
print("(1) ADMIN")
print("(2) USER")
print()
choice = numinput("Enter your choice: ")
print()


if choice >= 1 and choice <= 2:
    if choice == 1:
        pwd = simpledialog.askstring("Password", "Enter your password:", show="*")
        if pwd == "admin123123" or pwd == "libraryroot123":
            print("Recognised as admin....")
            print("Accessing administrative functions.....")
            print()
            time.sleep(2)
            while True:
                print("\t(1) Book functions")
                print("\t(2) Patron functions")
                print("\t(3) Transactions and Returns")
                print("\t(4) Exit")

                acc = numinput("\tPLEASE ENTER THE OPTION NUMBER : ")
                if acc >= 1 and acc <= 4:
                    if acc == 1:
                        print("\tAccessing........")
                        time.sleep(2)

                        while True:  #
                            print("\t\t**** BOOK FUNCTIONS ****")
                            print("\t\t OPTIONS : ")
                            print("\t\t(1) Add a book")
                            print("\t\t(2) Remove a book")
                            print("\t\t(3) Update a book")
                            print("\t\t(4) Issue a Book")
                            print("\t\t(5) Return a Book")
                            print("\t\t(6) Search a Book")
                            print("\t\t(7) View all books")
                            print("\t\t(8) Go back to main menu")
                            print("\t\t(9) Exit")

                            opt = numinput("\t\tPLEASE ENTER THE OPTION NUMBER : ")
                            if opt >= 1 and opt <= 9:
                                if opt == 1:
                                    nISBN = triminput("\t\tISBN : ")
                                    nTITLE = triminput("\t\tTITLE : ")
                                    nAUTHOR = triminput("\t\tAUTHOR : ")
                                    nGENRE = triminput("\t\tGENRE (Fiction/Non-Fiction): ")
                                    Quantity = numinput("\t\tQUANTITY : ")
                                    out = db.AddBook(Quantity, nTITLE, nAUTHOR, nISBN, nGENRE)
                                    if out != 1:
                                        print("\t\tBook added successfully!")
                                elif opt == 2:
                                    ISBN = triminput("\t\tISBN : ")
                                    out = db.RemoveBook(ISBN)
                                    if out != 1:
                                        print("\t\tBook removed successfully!")
                                elif opt == 3:
                                    ISBN = triminput("\t\tISBN : ")
                                    out = db.EditBook(ISBN)
                                    if out != 1:
                                        print("\t\tBook updated successfully!")
                                elif opt == 4:
                                    ISBN = triminput("\t\tISBN : ")
                                    ID = triminput("\t\tID of the patron: ")
                                    out = db.IssueBook(ISBN, ID)
                                    if out != 1:
                                        print("\t\tBook issued successfully!")
                                elif opt == 5:
                                    ISBN = triminput("\t\tISBN : ")
                                    ID = triminput("\t\tID of the patron: ")
                                    out = db.ReturnBook(ISBN, ID)
                                    if out != 1:
                                        print("\t\tBook returned successfully!")
                                elif opt == 6:
                                    while True:
                                        print("\t\t\t OPTIONS :")
                                        print("\t\t\t(1) By ISBN number")
                                        print("\t\t\t(2) By Author")
                                        print("\t\t\t(3) By Title")
                                        print("\t\t\t(4) By Genre")
                                        print("\t\t\t(5) Return to previous menu")
                                        print("\t\t\t(6) Exit")

                                        x = numinput("\t\t\tPLEASE ENTER THE OPTION NUMBER : ")
                                        if x >= 1 and x <= 6:
                                            if x == 1:
                                                ISBN = triminput("\t\t\t\tISBN : ")
                                                res = db.SearchBookByISBN(ISBN)
                                                if res != 1:
                                                    data, columns = res
                                                    print(tabulate(data, headers=columns, tablefmt="pretty"))
                                                else:
                                                    print("\t\t\t\tBook not found!")

                                            elif x == 2:
                                                Author = triminput("\t\t\t\tAuthor : ")
                                                res = db.SearchBookByAuthor(Author)
                                                if res != 1:
                                                    data, columns = res
                                                    print(tabulate(data, headers=columns, tablefmt="pretty"))
                                                else:
                                                    print("\t\t\t\tBook not found!")

                                            elif x == 3:
                                                Title = triminput("\t\t\t\tTitle : ")
                                                res = db.SearchBookByTitle(Title)
                                                if res != 1:
                                                    data, columns = res
                                                    print(tabulate(data, headers=columns, tablefmt="pretty"))
                                                else:
                                                    print("\t\t\t\tBook not found!")
                                                    break
                                            elif x == 4:
                                                Genre = triminput("\t\t\t\tGenre : ")
                                                res = db.SearchBookByGenre(Genre)
                                                if res != 1:
                                                    data, columns = res
                                                    print(tabulate(data, headers=columns, tablefmt="pretty"))
                                                else:
                                                    print("\t\t\t\tBook not found!")
                                                    break
                                            elif x == 5:
                                                break
                                            elif x == 6:
                                                exit()
                                        else:
                                            print("\t\t\tIncorrect option entered!")
                                elif opt == 7:
                                    db.ViewBooks()
                                elif opt == 8:
                                    break
                                elif opt == 9:
                                    exit()
                            else:
                                print("\t\t\Incorrect option entered!")
                    elif acc == 2:
                        print("\tAccessing........")
                        time.sleep(2)

                        while True:
                            print("\t\t**** PATRON FUNCTIONS ****")
                            print("\t\t OPTIONS : ")
                            print("\t\t(1) Add Patron")
                            print("\t\t(2) Remove Patron")
                            print("\t\t(3) Update Patron")
                            print("\t\t(4) Search Patron")
                            print("\t\t(5) View Patrons")
                            print("\t\t(6) Go back to main menu")
                            print("\t\t(7) Exit")
                            opt = numinput("\t\tPLEASE ENTER THE OPTION NUMBER : ")
                            if opt >= 1 and opt <= 7:
                                if opt == 1:
                                    ID = triminput("\t\tID : ")
                                    Email = triminput("\t\tEmail : ")
                                    Patron_Name = triminput("\t\tPatron Name : ")
                                    Subcription_Date = triminput("\t\tEnter Date(YYYY-MM-DD) : ")
                                    if not validate_date(Subcription_Date):
                                        print("\t\t\tIncorrect date entered!")
                                        break
                                    db.AddPatron(ID, Email, Patron_Name, Subcription_Date)
                                elif opt == 2:
                                    ID = triminput("\t\tID : ")
                                    db.RemovePatron(ID)
                                elif opt == 3:
                                    ID = triminput("\t\tID : ")
                                    db.EditPatron(ID)
                                elif opt == 4:
                                    while True:
                                        print("\t\t\t OPTIONS :")
                                        print("\t\t\t(1) By ID")
                                        print("\t\t\t(2) By Name")
                                        print("\t\t\t(3) Return to previous menu")
                                        print("\t\t\t(4) Exit")
                                        x = numinput("\t\t\tPLEASE ENTER THE OPTION NUMBER : ")
                                        if x >= 1 and x <= 4:
                                            if x == 1:
                                                ID = triminput("\t\t\tID : ")
                                                res = db.SearchPatronByID(ID)
                                                if res != 1:
                                                    data, columns = res
                                                    print(tabulate(data, headers=columns, tablefmt="pretty"))
                                                else:
                                                    print("\t\t\t\tPatron not found!")
                                                    break
                                            elif x == 2:
                                                Name = triminput("\t\t\tName : ")
                                                res = db.SearchPatronByName(Name)
                                                if res != 1:
                                                    data, columns = res
                                                    print(tabulate(data, headers=columns, tablefmt="pretty"))
                                                else:
                                                    print("\t\t\t\tPatron not found!")
                                                    break
                                            elif x == 3:
                                                break
                                            elif x == 4:
                                                exit()
                                        else:
                                            print("Incorrect option entered!")
                                elif opt == 5:
                                    db.ViewPatrons()
                                elif opt == 6:
                                    break
                                elif opt == 7:
                                    exit()
                            else:
                                print("Incorrect option entered!")
                    elif acc == 3:
                        print("\tAccessing........")
                        time.sleep(2)

                        while True:
                            print("\t\t**** TRANSACTIONS ****")
                            print("\t\t OPTIONS : ")
                            print("\t\t(1) View Transactions")
                            print("\t\t(2) View all pending returns")
                            print("\t\t(3) Return to previous menu")
                            print("\t\t(4) Exit")

                            opt = numinput("\t\tPLEASE ENTER THE OPTION NUMBER : ")
                            if opt >= 1 and opt <= 4:
                                if opt == 1:
                                    db.ViewTransactions()
                                elif opt == 2:
                                    db.ViewTransactionsPending()
                                elif opt == 3:
                                    break
                                elif opt == 4:
                                    exit()
                            else:
                                print("Incorrect option entered!")
                    elif acc == 4:
                        exit()
                else:
                    print("Incorrect option entered!")
        else:
            print("Wrong Password !!")
            exit()
    elif choice == 2:
        ID = simpledialog.askstring("ID", "Enter your Patron ID:")
        if db.SearchPatronByID(ID) == 1:
            print("Patron ID not found !!")
            exit()
        else:
            print("Recognised as our registered patron....")
            print("Accessing patron functions.....")
            print()
            time.sleep(2)
            while True:
                print("\tOPTIONS :")
                print("\t(1) Search a book")
                print("\t(2) View all books")
                print("\t(3) View my issued books")
                print("\t(4) Exit")
                acc = numinput("\tPLEASE ENTER THE OPTION NUMBER : ")
                if acc >= 1 and acc <= 4:
                    if acc == 1:
                        while True:
                            print("\t\t OPTIONS :")
                            print("\t\t(1) By ISBN number")
                            print("\t\t(2) By Author")
                            print("\t\t(3) By Title")
                            print("\t\t(4) By Genre")
                            print("\t\t(5) Return to previous menu")
                            print("\t\t(6) Exit")
                            x = numinput("\t\t\tPLEASE ENTER THE OPTION NUMBER : ")
                            if x >= 1 and x <= 6:
                                if x == 1:
                                    ISBN = triminput("\t\t\tISBN : ")
                                    res = db.SearchBookByISBN(ISBN)
                                    if res != 1:
                                        data, columns = res
                                        print(tabulate(data, headers=columns, tablefmt="psql"))
                                    else:
                                        print("\t\t\t\tBook not found!")
                                        break
                                elif x == 2:
                                    Author = triminput("\t\t\tAuthor : ")
                                    res = db.SearchBookByAuthor(Author)
                                    if res != 1:
                                        data, columns = res
                                        print(tabulate(data, headers=columns, tablefmt="pretty"))
                                    else:
                                        print("\t\t\t\tBook not found!")
                                        break
                                elif x == 3:
                                    Title = triminput("\t\t\tTitle : ")
                                    res = db.SearchBookByTitle(Title)
                                    if res != 1:
                                        data, columns = res
                                        print(tabulate(data, headers=columns, tablefmt="pretty"))
                                    else:
                                        print("\t\t\t\tBook not found!")
                                        break
                                elif x == 4:
                                    Genre = triminput("\t\t\tGenre : ")
                                    res = db.SearchBookByGenre(Genre)
                                    if res != 1:
                                        data, columns = res
                                        print(tabulate(data, headers=columns, tablefmt="pretty"))
                                    else:
                                        db.SearchBookByAuthor(Author)
                                elif x == 5:
                                    break
                                elif x == 6:
                                    exit()
                    elif acc == 2:
                        db.ViewBooks()
                    elif acc == 3:
                        query = """SELECT 
                            b.title "Book", 
                            p.name "Issued by", 
                            t.issue_date "Issued On", 
                            t.due_date "Due Date", 
                            IFNULL(t.return_date, \'Not Returned\') \'Returned On\' 
                        FROM transactions t 
                        JOIN books b ON t.book_isbn = b.isbn 
                        JOIN patrons p ON p.id = t.patron_id 
                        WHERE t.patron_id = %s"""
                        res = db.Query(query, (ID,))
                        if res != 1:
                            data, columns = res
                            print(tabulate(data, headers=columns, tablefmt="pretty", stralign="center"))
                        else:
                            print("\t\t\t\tNo books issued!")
                    elif acc == 4:
                        exit()
                else:
                    print("Incorrect option entered!")
else:
    print("Incorrect option entered!")
