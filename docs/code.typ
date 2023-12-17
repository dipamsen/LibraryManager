#import "@preview/sourcerer:0.2.1": code

#let code = code.with(
  number-align: right,
  line-offset: 10pt,
  text-style: (tracking: -0.09pt),
)


#let codes = [
   
  #set text(12pt)
   
  == `main.py` <main-py> 
   
  #code(raw(read("../src/main.py"), lang: "py"))
   
   
   
  // #pagebreak(weak: true)
  == `database.py` <database-py> 
   
  #code(raw(read("../src/database.py"), lang: "py"))
   
   
  // #pagebreak(weak: true)
  == `db.sql` <db-sql> 
   
  #code(raw(read("../src/db.sql"), lang: "sql"))
   
]




#let screenshots = [
  // #let images = (
  //   "pass",
  //   "adminfn",
  //   "searchbook",
  //   "viewbooks",
  //   "viewtrans",
  //   "patronfn",
  //   "viewissued",
  // )
   
  // #for img in images {
  //   image("screenshots/" + img + ".png", fit: "contain")
  // }
  #set heading(outlined: false)
  #set block(spacing: 7pt)
  Welcome Screen
  #image("screenshots/welcome.png")
  == 1. Admin Screens
  #image("screenshots/admin.login.png", width: 90%)
  #image("screenshots/admin.menu.png")
  #pagebreak(weak: true)
  *(a) Book Functions*
  #image("screenshots/admin.book.menu.png", width: 90%)
  Add a Book
  #image("screenshots/admin.book.add.png", width: 90%)
  View all Books
  #image("screenshots/admin.book.view.png")
  #pagebreak(weak: true)
  Issue a Book
  #image("screenshots/admin.book.issue.png", width: 90%)
  Return a Book
  #image("screenshots/admin.book.return.png", width: 90%)
  Update book quantity
  #image("screenshots/admin.book.update.png", width: 90%)
  Search Book
  #image("screenshots/admin.book.search.png", width: 90%)
  Remove a Book
  #image("screenshots/admin.book.remove.png", width: 90%)
  #pagebreak(weak: true)
   
  *(b) Patron Functions*
  #image("screenshots/admin.patron.menu.png", width: 80%)
  View Patrons
  #image("screenshots/admin.patron.view.png")
  Add a Patron
  #image("screenshots/admin.patron.add.png", width: 90%)
  Update Patron
  #image("screenshots/admin.patron.edit.png")
  Search Patron
  #image("screenshots/admin.patron.search.png")
  Remove a Patron
  #image("screenshots/admin.patron.remove.png", width: 90%)
   
  *(c) Transaction Functions*
  #image("screenshots/admin.transactions.menu.png")
  View Transactions
  #image("screenshots/admin.transactions.view.png")
  #pagebreak(weak: true)
  View Pending Transactions
  #image("screenshots/admin.transactions.viewPending.png")
   
  == 2. Patron Screens
  #image("screenshots/patron.login.png", width: 90%)
  #image("screenshots/patron.menu.png")
  View books
  #image("screenshots/patron.view.png")
  #pagebreak(weak: true)
  Search books
  #image("screenshots/patron.search.png")
  Issue a book
  #image("screenshots/patron.issue.png", width: 90%)
  View Issued Books
  #image("screenshots/patron.viewIssued.png")
  Return a book
  #image("screenshots/patron.return.png", width: 90%)
   
   
]
