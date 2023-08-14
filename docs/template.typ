#let bigheading(content) = {
  text(35pt, align(center, heading(content)))
  text(1em)[\ ]
}

#let field = (it, col: rgb(204, 51, 139)) => box.with(
    fill: luma(240), outset: (top: 4pt, bottom: 4pt), inset: (left: 4pt, right: 4pt),  radius: 4pt,
  )(text(it, fill: col))

#let name = "Dipam Sen"
  
  
#let project(
  title: "",
  authors: (),
  date: none,
  logo: none,
  body,
) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: (p, ..) => if p > 1 {p}, number-align: center)
  set text(font: "", lang: "en", size: 1.6em)
  set text(font: "Atkinson Hyperlegible")
  // show raw: it => {
  //   if it.block {
  //     par(text(0.8em)[#it], justify: false, linebreaks: "simple")
  //   } else {
  //     strong(it)
  //   }
  // }
  show link: underline

  // https://discord.com/channels/1054443721975922748/1057632212671025162/1105957435178496061
  // Display block code in a larger block
  // with more padding and line numbers on the left
  // show raw.where(block: true): it => {
  //   set par(justify: false);
  //   // the line counter
  //   let boxRadius = 0.5em;
  //   let detailRadius = 3pt;
  //   if (it.lang != none) {
  //     grid(
  //       block(radius: boxRadius, fill: luma(246), width: 100%, inset: boxRadius*2.4, {
  //         it
  //       })
  //     )
  //   } else {
  //     block(radius: boxRadius, fill: luma(246), width: 100%, inset: boxRadius, it)
  //   }
  // }
  {
    set text(1.3em)

    {
      set align(center)
      v(1.2em, weak: true)
      text(1.1em, weight: 600, underline("Amicus International School, Bharuch"))
      v(3em, weak: true)
      // title
      // 
      text(1.1em, weight: 700)[PROJECT REPORT ON]
      v(1.4em, weak: true)
      text(2em, strong[SOFTWARE FOR])
      v(1.4em, weak: true)
      text(2em, weight: 700)[Library Management]
      v(2em, weak: true)
      text(1.6em, "Computer Science Project")
      v(2em)
    pad(
      top: 0.7em,
    [Created By:]+
      // right: 20%,
      box(grid(
        // columns: 2, //(30pt, 1fr, 1fr, 1fr), //(1fr,) * calc.min(3, authors.len()),
        gutter: 0.7em,
        ..authors.map(author => align(start, text(author, weight: "black"))),
      ), baseline:2.2cm, inset: (left: 1em)),
    )
    
    }
    
    // Author information.
  }
  v(2.4fr)
  pagebreak()


  
  bigheading("Certificate")
  {
    show par: set block(spacing: 1em)
    par(justify: true, first-line-indent: 1em, leading: 1em, text(size: 1.2em, hyphenate: false, tracking: 1pt)[
      This is to certify that *#name* of Class XII-B, have successfully completed the investigatory project on the topic *#title.slice(18)* under the guidance of Mrs. Arpita Bhoi during the academic year 2023-24 in the partial fulfillment of Practical Examination conducted by CBSE. 

      
    ])

    [
      #v(8cm)
      #set text(1em)
      #set align(center)

      #let people = ("Internal Examiner", "Principal", "External Examiner")
      #let sign(person) = par(justify: false)[#line(length: 4.5cm, stroke: 2pt)
      Signature of #person]
      #grid(
        columns: 3, 
          ..people.map(sign)
        )
    ]
  }
  pagebreak()

  bigheading("Acknowledgements")

  {
    show par: set block(below: 2em)
    par(justify: true, leading: 1.08em, text(1.1em, hyphenate: false)[
      I extend my heartfelt gratitude to everyone who has
contributed to the completion of this Project.

I am sincerely grateful to our principal Mrs. Thresiamma
Pappachan and my CS teacher Mrs. Arpita Bhoi. Their unwavering support and guidance have been instrumental in its completion.

Lastly, I express my sincere gratitude to my parents
and family for their unwavering support.

To all those mentioned above and many others who
have directly or indirectly contributed, your support
has been truly invaluable in my growth as a learner.

#align(right)[
  \- #name
]
    ])
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