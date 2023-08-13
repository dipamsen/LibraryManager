# Library Manager
# Author: Dipam Sen and Arghya Kumar

import data as db
from utils import ask_choices, highlight, bold
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
            choice = ask_choices(
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
            if "action" in choice:
                choice["action"]()

            func = choice["value"]
            desc = choice["text"]
            args = inspect.getfullargspec(func).args

            print(f"\nPerforming the operation: {desc}\n")

            if args:
                print(args, "\n")

            output = None
            if not args:
                output = func()
            else:
                args_input = [input(f"Enter {arg}: ") for arg in args]
                output = func(*args_input)

            if output == 1:
                print("\nSomething went wrong. Please try again.")
            else:
                print("\nSuccessfully performed the operation!\n")

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
        choice = ask_choices(
            [
                {"text": "View all books", "q": "SELECT * FROM books", "args": []},
                {
                    "text": "View my issued books",
                    "q": f'SELECT b.title "Book", p.name "Issued by", t.issue_date "Issued On", t.due_date "Due Date", IFNULL(t.return_date, \'Not Returned\') \'Returned On\', IF(t.due_date < CURDATE() AND NOT t.returned, "{highlight("Overdue")}", "") "Overdue" FROM transactions t JOIN books b ON t.book_isbn = b.isbn JOIN patrons p ON p.id = t.patron_id WHERE t.patron_id = %s',
                    "args": [id],
                },
                {"text": "Exit", "action": exit},
            ]
        )
        if "action" in choice:
            choice["action"]()
        query = choice["q"]
        desc = choice["text"]
        args = choice["args"]
        print()
        print(f"Performing the operation: {desc}")
        print()
        output = db.Query(query, tuple(args))
        if output == 1:
            print()
            print("Something went wrong. Please try again.")
        else:
            print(
                tabulate(
                    output[0],
                    headers=[bold(h) for h in output[1]],
                    tablefmt="rounded_outline",
                )
            )
            print()
            print("Successfully performed the operation!")

        print()
elif choice == 3:
    exit()
