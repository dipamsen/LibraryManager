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
  #let images = (
    "pass",
    "adminfn",
    "searchbook",
    "viewbooks",
    "viewtrans",
    "patronfn",
    "viewissued",
  )
   
  #for img in images {
    image("screenshots/" + img + ".png", fit: "contain")
  }
]
