from tkinter import simpledialog
import database as db
import utils

print("Welcome to Library Manager!")
print()
print("ACCESS TO:")
print("(1) ADMIN")
print("(2) PATRON")
print()
choice = utils.num_input("Enter your choice: ")
print()

if choice == 1:
    pwd = simpledialog.askstring("Password", "Enter password:", show="*")
    if pwd == "admin":
        print("ACCESS GRANTED!")
        print()
        while True:
            print("(1) Books")
            print("(2) Patrons")
            print("(3) Transactions and Requests")

            choice = utils.num_input("Enter your choice: ")
            print()

            if choice == 1:
                while True:
                    print("\tManage Books")
                    print() 
                    print("\t(1) Add Book")
                    print("\t(2) Remove Book")
                    print("\t(3) Update Book Quantity")
                    print("\t(4) Issue Book")
                    print("\t(5) Return Book")
                    print("\t(6) Search Book")
                    print("\t(7) Show All Books")
                    print("\t(B) Go Back")
                    print("\t(Q) Quit")
                    print()
                    choice = utils.trim_input("\tEnter your choice: ")
                    print()

                    if choice == "1":
                        print("\t\tAdd Book")
                        print()
                        isbn = utils.validate_isbn(utils.trim_input("\t\tEnter ISBN: "))
                        title = utils.trim_input("\t\tEnter Title: ")
                        author = utils.trim_input("\t\tEnter Author: ")
                        quantity = utils.num_input("\t\tEnter Quantity: ")
                        print()
                        if isbn and title and author and quantity:
                            db.update_query("INSERT INTO books (isbn, title, author, quantity) VALUES (%s, %s, %s, %s)", (isbn, title, author, quantity))
                            print("\t\tBook added successfully!")
                        else:
                            print("\t\tInvalid Input!")
                        print()
                    elif choice == "2":
                        print("\t\tRemove Book")
                        print()
                        isbn = utils.trim_input("\t\tEnter ISBN: ")
                        print()
                        if isbn:
                            try:
                                db.update_query("DELETE FROM books WHERE isbn = %s", (isbn,))
                                print("\t\tBook removed successfully!")
                            except:
                                print("\t\tBook not found!")
                        else:
                            print("\t\tInvalid Input!")
                        print()
                    elif choice == "3":
                        print("\t\tUpdate Book Quantity")
                        print()
                        isbn = utils.trim_input("\t\tEnter ISBN: ")
                        quantity = utils.num_input("\t\tEnter new quantity: ")
                        print()
                        if isbn and quantity:
                            try:
                                db.update_query("UPDATE books SET quantity = %s WHERE isbn = %s", (quantity, isbn))
                                print("\t\tBook quantity updated successfully!")
                            except:
                                print("\t\tBook not found!")
                        else:
                            print("\t\tInvalid Input!")
                        print()
                    elif choice == "4":
                        print("\t\tIssue Book")
                        print()
                        isbn = utils.trim_input("\t\tEnter ISBN: ")
                        patron_id = utils.num_input("\t\tEnter Patron ID: ")
                        print()
                        if isbn and patron_id:
                            try:
                                db.issue_book(isbn, patron_id)
                                print("\t\tBook issued successfully!")
                            except Exception as e:
                                print("\t\t", e)
                                
                        else:
                            print("\t\tInvalid Input!")
                        print()



