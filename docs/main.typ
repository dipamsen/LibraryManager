#import "template.typ": *
#import "code.typ": code

#show: project.with(
  title: "Project Report on Software for Library Management",
  authors: (
    "Dipam Sen",
    "Arghya Kumar",
  ),
  date: "2023",
)

= Introduction
#lorem(60)

Thus, we'll use the `mysql` module

= Technologies used

This project uses Python as the primary programming language for the frontend application. The project uses an MySQL database for the backend, for efficient data storage and retrieval.


= Functional Requirements

The following are the functional requirements for a library management system:

- To list and search books by criteria
- To add, remove and update books
- To view information about patrons
- To issue books and return books
- To view information about book issuance

= Code

The complete source code for the application as well as this document is accessible on the GitHub repository for the project:
https://github.com/dipamsen/LibraryManager

#code