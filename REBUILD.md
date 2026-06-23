# Rebuild this project's environment

Dependency folders (`.venv` / `node_modules`) do not carry across machines or Windows profiles.
Run the steps below once after moving or cloning this project.

## Python - `requirements.txt`

```
# from: .
py -3.12 -m venv .venv          # Windows (use python3.12 on Mac)
.venv\Scripts\python -m pip install -r "requirements.txt"   # Windows
.venv/bin/python -m pip install -r "requirements.txt"       # Mac
```
Use Python 3.12 (3.14 lacks wheels for some packages).

