#import "@preview/tablex:0.0.6":tablex, gridx, cellx, colspanx, rowspanx

#let bigheading(content, outlined: false, ..args) = {
  text(
    size: 35pt,
    align(center, heading(content, outlined: outlined)),
    ..args,
  )
  text(1em)[\ ]
}

#let field = (it, col: rgb(204, 51, 139)) => box.with(
  fill: luma(240),
  outset: (top: 4pt, bottom: 4pt),
  inset: (left: 4pt, right: 4pt),
  radius: 4pt,
)(text(it, fill: col))

#let name = "Arghya Kumar"
 
 
#let project(title: "", authors: (), date: none, logo: none, body) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(
    numbering: (p, ..) => if p > 2 { p },
    number-align: center,
    background: rect(
      width: 90%,
      height: 90%,
      outset: (bottom: 16pt),
      stroke: (thickness: 3pt, dash: "solid"),
    ),
  )
  set text(font: "Atkinson Hyperlegible", lang: "en", size: 1.6em)
   
  show link: underline
   
  {
    set page(background: [
      #rect(
        [
          #v(2em)
          #image("liblogo.png", width: 90%)
        ],
        width: 90%,
        height: 90%,
        outset: (bottom: 16pt),
        stroke: (thickness: 3pt, dash: "solid"),
      )
    ])
    set text(1.3em)
     
    {
      set align(center)
      v(1.2em, weak: true)
      text(0.9em, weight: 700, upper("Amicus International School, Bharuch"))
      v(0.7em, weak: true)
      image("aislogo.jpg", width: 100pt)
      v(1em, weak: true)
      text(0.9em, weight: 700, underline[Academic Year: 2023-24])
      v(2em, weak: true)
      // title
      // 
      text(1.1em, weight: 700)[PROJECT REPORT ON]
      v(1.4em, weak: true)
      text(2em, strong[SOFTWARE FOR])
      v(1.4em, weak: true)
      text(2.05em, weight: 700)[Library Management]
      v(2em, weak: true)
      text(1.6em, "Computer Science Project")
      v(7em)
      set text(0.8em)
      set align(left)
      let namelist = gridx(
        columns: 2,
        row-gutter: 0.2em,
        map-cells: cell => {
          if cell.x == 0 {
            cell.content = strong(cell.content)
          }
          if cell.y == 0 {
            cell.content = underline(cell.content)
          }
          if cell.x == 1 {
            cell.content += place(line(length: 130pt), bottom, dy: 2pt)
          }
          return cell
        },
        colspanx(2)[Submitted By:],
        [Name:],
        name,
        [Class:],
        "XII-B",
        [Roll No.:],
        [],
      )
       
      let guide = gridx(columns: 1, row-gutter: 0.2em, map-cells: cell => {
        if cell.y == 0 {
          cell.content = strong(cell.content)
        }
        return cell
      }, [Project Guide], [Mrs. Arpita Bhoi], [PGT (Computer Science)])
       
      place(
        block(grid(columns: 2, gutter: 1fr, namelist, guide), width: 110%),
        dx: -5%,
      )
    }
  }
  pagebreak(weak: true)
   
  let dsg = if name.contains("Kansara") { "Miss" } else { "Master" }
   
  // {
  //   set align(center)
  //   text(1.2em, weight: 600, upper("Amicus International School, Bharuch"))
  //   v(0.7em, weak: true)
  //   image("aislogo.jpg", width: 80pt)
  //   v(1em, weak: true)
  // }
  bigheading("Certificate", font: "Old English Text MT", size: 48pt)
  {
    show par: set block(spacing: 1em)
    par(
      justify: true,
      first-line-indent: 1em,
      leading: 1em,
      text(
        size: 1.2em,
        hyphenate: false,
        tracking: 1pt,
      )[
        This is to certify that #dsg *#name* of *Class XII-B (Science)*, has
        successfully completed the *Computer Science (083)* investigatory project on the
        topic *#title.slice(18)* within the stipulated time frame with sincerity and
        devotion, under the guidance of Mrs. Arpita Bhoi during the academic year
        2023-24 in the partial fulfillment of Practical Examination conducted by CBSE.
      ],
    )
     
    [
      #v(2cm)
      #set text(1em)
      #set align(center)
       
      #let people = ("Internal Examiner", "Principal", "External Examiner")
      #let sign(person) = par(justify: false)[#line(length: 4.5cm, stroke: 2pt)
        Signature of #person]
      #grid(columns: 3, gutter: 1em, ..people.map(sign))
      #set align(left)
      #v(1.2cm)
      #let under = place(bottom, line(length: 4.5cm, stroke: 2pt))
      #grid(columns: 2, gutter: 0.8em, [Date:], under, [Place:], under)
    ]
  }
  pagebreak()
   
  bigheading("Acknowledgement")
   
  {
    show par: set block(below: 2em)
    par(
      justify: true,
      leading: 1.08em,
      text(
        1.1em,
        hyphenate: false,
      )[
        I extend my heartfelt gratitude to everyone who has contributed to the
        completion of this Project.
         
        I am sincerely grateful to our principal Mrs. Thresiamma Pappachan and my CS
        teacher Mrs. Arpita Bhoi. Their unwavering support and guidance have been
        instrumental in its completion.
         
        Lastly, I express my sincere gratitude to my parents and family for their
        unwavering support.
         
        To all those mentioned above and many others who have directly or indirectly
        contributed, your support has been truly invaluable in my growth as a learner.
         
        #align(right)[
          \- #name
        ]
      ],
    )
  }
   
  pagebreak(weak: true)
   
  // Table of contents.
  bigheading("Index")
  {
    set text(1.1em)
    outline(depth: 3, indent: 1em, title: none)
  } 
  pagebreak()
   
   
  // Main body.
  set par(justify: true)
  set text(hyphenate: false)
   
  body
}