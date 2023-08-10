# Library Manager
# Author: Dipam Sen and Arghya Kumar

import data as db
from utils import ask_choices
import inspect
from tabulate import tabulate

print("Welcome to the Library Manager!!")
print()

print("1. ADMIN")
print("2. USER")
print("3. EXIT")

choice = int(input("Enter your choice: "))
print()

if choice == 1:
    pwd = input("Enter the password: ")
    if pwd == "admin":
        while True:
            val = ask_choices(
                [
                    {"text": "Add a book", "value": db.AddBook},
                    {"text": "Remove a book", "value": db.RemoveBook},
                    {"text": "Update a book", "value": db.EditBook},
                    {"text": "Add a patron", "value": db.AddPatron},
                    {"text": "Remove a patron", "value": db.RemovePatron},
                    {"text": "Update a patron", "value": db.EditPatron},
                    {"text": "View all books", "value": db.ViewBooks},
                    {"text": "View all patrons", "value": db.ViewPatrons},
                    {"text": "Issue a book", "value": db.IssueBook},
                    {"text": "Return a book", "value": db.ReturnBook},
                    {"text": "View all transactions", "value": db.ViewTransactions},
                    {
                        "text": "View all pending returns",
                        "value": db.ViewTransactionsPending,
                    },
                    {"text": "Exit", "action": exit},
                ]
            )
            if "action" in val:
                val["action"]()
            func = val["value"]
            desc = val["text"]
            ins = inspect.getfullargspec(func)  # Get the arguments of the function
            args = ins[0]
            print()
            print(f"Performing the operation: {desc}")
            print()
            if args:
                print(args)
                print()
            out = None
            if len(args) == 0:
                out = func()
            else:
                out = func(*[input(f"Enter {arg}: ") for arg in args])
            if out == 1:
                print()
                print("Something went wrong. Please try again.")
            else:
                print()
                print("Successfully performed the operation!")
            print()

elif choice == 2:
    patrons = db.Query("SELECT name, id FROM patrons")[0]
    print("List of patrons:")
    for i, patron in enumerate(patrons):
        print(f"{i+1}. {patron[0]}")
    print()
    patron = patrons[int(input("Enter your choice: ")) - 1]
    print()
    print(f"Welcome {patron[0]}!")
    print()
    name = patron[0]
    id = patron[1]
    while True:
        val = ask_choices(
            [
                {"text": "View all books", "q": "SELECT * FROM books", "args": []},
                {
                    "text": "View my issued books",
                    "q": "SELECT b.isbn, t.patron_id, t.issue_date, t.due_date, IFNULL(t.return_date, 'Not Returned') 'return_date' FROM transactions t JOIN books b ON t.book_isbn = b.isbn WHERE t.patron_id = %s",
                    "args": [id],
                },
                {"text": "Exit", "action": exit},
            ]
        )
        if "action" in val:
            val["action"]()
        query = val["q"]
        desc = val["text"]
        args = val["args"]
        print()
        print(f"Performing the operation: {desc}")
        print()
        out = db.Query(query, tuple(args))
        if out == 1:
            print()
            print("Something went wrong. Please try again.")
        else:
            print(tabulate(out[0], headers=out[1], tablefmt="psql"))
            print()
            print("Successfully performed the operation!")

        print()
elif choice == 3:
    exit()
