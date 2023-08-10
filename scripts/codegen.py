# Library Manager
"""
Creates a `docs/code.typ` file from the source code in `src/` to be used in the project report.
"""

import os

if __name__ == "__main__":
    codes = {}
    root, dirs, files = next(os.walk("src"))
    files = ["data.py", "db.sql"]
    for filename in files:
        # if filename.endswith(".py"):
        if filename.startswith(".env"):
            continue
        with open(os.path.join(root, filename), "r") as f:
            codes[filename] = f.read()

    code = """#import "@preview/codelst:1.0.0": *
    
#let code = [\n\n  #set text(0.67em)\n\n"""
    for filename, content in codes.items():
        code += f"== `{filename}`\n\n#sourcecode(numbering: none)[```{filename.rpartition('.')[-1]}\n{content}\n```]\n\n"
    code += "]"

    with open("docs/code.typ", "w") as f:
        f.write(code)
