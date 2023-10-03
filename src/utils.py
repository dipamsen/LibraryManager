
import time

def validate_date(date):
    """Checks whether date is in correct format (yyyy-mm-dd)."""
    # yyyy-mm-dd
    try:
        time.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def trim_input(*args, **kwargs):
    """Returns a stripped string from user input."""
    return input(*args, **kwargs).strip()

def num_input(*args, **kwargs):
    """Returns an integer from user input."""
    while True:
        try:
            return int(input(*args, **kwargs))
        except ValueError:
            print("Invalid input! Please enter a number.")

def validate_isbn(isbn):
    """Returns formatted ISBN if valid, False otherwise."""
    # Remove hyphens and spaces
    isbn = isbn.replace("-", "").replace(" ", "")

    # ISBN-10
    if len(isbn) == 10:
        if not isbn[:-1].isdigit():
            return False
        if isbn[-1].upper() == "X":
            isbn_sum = (
                sum(int(digit) * (i + 1) for i, digit in enumerate(isbn[:-1])) + 10
            )
        else:
            isbn_sum = sum(int(digit) * (i + 1) for i, digit in enumerate(isbn))
        return isbn if isbn_sum % 11 == 0 else False

    # ISBN-13
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
        isbn_sum = sum(
            int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn)
        )
        return isbn if isbn_sum % 10 == 0 else False

    return False
