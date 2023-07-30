  


#let project(
  title: "",
  authors: (),
  date: none,
  logo: none,
  body,
) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: "1", number-align: center)
  set text(font: "", lang: "en", size: 1.6em)
  show raw: it => {
    if it.block {
      par(text(0.8em)[#it], justify: false, linebreaks: "simple")
    } else {
      strong(it)
    }
  }
  show link: underline

  // https://discord.com/channels/1054443721975922748/1057632212671025162/1105957435178496061
  // Display block code in a larger block
  // with more padding and line numbers on the left
  show raw.where(block: true): it => {
    set par(justify: false);
    // the line counter
    let boxRadius = 0.5em;
    let detailRadius = 3pt;
    if (it.lang != none) {
      grid(
        block(radius: boxRadius, fill: luma(246), width: 100%, inset: boxRadius*2.4, {
          it
        })
      )
    } else {
      block(radius: boxRadius, fill: luma(246), width: 100%, inset: boxRadius, it)
    }
  }
  {
    set text(1.3em)
    v(0.6fr)
    if logo != none {
      align(right, image(logo, width: 26%))
    }
    v(9.6fr)
  
    v(1.2em, weak: true)
    text(1.1em, date)
    v(1.2em, weak: true)
    text(2em, weight: 700, title)
    v(1.2em, weak: true)
  
    smallcaps("Computer Science Project")
    v(2em)
  
    // Author information.
    pad(
      top: 0.7em,
      right: 20%,
      grid(
        columns: (1fr,) * calc.min(3, authors.len()),
        gutter: 1em,
        ..authors.map(author => align(start, strong(author))),
      ),
    )
  }
  v(2.4fr)
  pagebreak()


  // Table of contents.
  outline(depth: 3, indent: 1em, title: "Table of Contents")
  pagebreak()


  // Main body.
  set par(justify: true)
  set text(hyphenate: false)

  body
}