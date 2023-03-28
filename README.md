# github-dependents

> Get the dependents of a GitHub repository



## Usage
Change the repo variable to the repository you want to get the dependents of:
```python
repo = "pyserial/pyserial"
```

```console
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
After that you will get a list of repositories that depend on the repository you specified.
In current version, the list is saved in the file `repo_name_stargazers.json` in the current directory.
in this case filename is `pyserial_stargazers.json`

File structure:
```json
[
    {
        "repo": "k0retux/fuddly",
        "stargazers": 160
    },
    {
        "repo": "DShield-ISC/dshield",
        "stargazers": 340
    },
    {
        "repo": "microsoft/PythonProgrammingPuzzles",
        "stargazers": 864
    },
    {
        "repo": "isl-org/OpenBot",
        "stargazers": 2369
    },
    {
        "repo": "micropython/micropython",
        "stargazers": 16179
    }
]
```
## MIT License
Copyright (c) 2023 Andrew Dorokhin