# Library Manager
"""
Creates a `docs/code.typ` file from the source code in `src/` to be used in the project report.
"""

import os

if __name__ == "__main__":
    codes = {}
    for root, dirs, files in os.walk("src"):
        for filename in files:
            if filename.endswith(".py"):
                with open(os.path.join(root, filename), "r") as f:
                    codes[filename] = f.read()

    code = "#let code = [\n\n"
    for filename, content in codes.items():
        code += f"== `{filename}`\n\n```py\n{content}\n```\n\n"
    code += "]"

    with open("docs/code.typ", "w") as f:
        f.write(code)
