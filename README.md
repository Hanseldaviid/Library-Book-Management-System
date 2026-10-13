# Python OOP - Library & Book Management System 📚

A Python project designed to demonstrate core concepts of **Object-Oriented Programming (OOP)**, including object composition, instance attributes, array iteration, and custom metric aggregations.

## Features

* **Book Modeling**: Store book details including title, author, total page count, and release year.
* **Catalog Management**: Add book objects dynamically to a library collection.
* **Interactive Display**: Print a formatted catalog listing all registered books and their metadata.
* **Data Aggregation**:
  * Count total books in the library using Python's `len()`.
  * Calculate total aggregate pages across all books using iterative loops.

## Technologies Used

* Python 3

## Code Overview

* **`Book` Class**: Encapsulates data for individual books (`title_book`, `author`, `pages`, `release_year`).
* **`Library` Class**: Manages a collection of `Book` instances using a list attribute (`self.books`), providing methods for adding books, rendering the catalog, counting entries, and summing pages.
