# Library Manager
"""
Creates a `docs/code.typ` file from the source code in `src/` to be used in the project report.
"""

import os


def slugify(text):
    return text.lower().replace(" ", "-").replace(".", "-")


def reptabs(text):
    return text.replace("    ", "  ")


if __name__ == "__main__":
    codes = {}
    root, dirs, files = next(os.walk("src"))
    files = ["main.py", "database.py", "db.sql"]
    for filename in files:
        with open(os.path.join(root, filename), "r") as f:
            codes[filename] = f.read()

    code = """#import "@preview/codelst:1.0.0": *
    
#let code = [\n\n  #set text(0.67em)\n\n"""
    for filename, content in codes.items():
        code += f"== `{filename}` <{slugify(filename)}> \n\n#sourcecode(numbering: none)[```{filename.rpartition('.')[-1]}\n{reptabs(content)}\n```]\n\n"
    code += "]"

    with open("docs/code.typ", "w") as f:
        f.write(code)
