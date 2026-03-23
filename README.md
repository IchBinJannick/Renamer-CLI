
# Renamer-CLI

A visually Command Line Interface (CLI) tool for efficient file renaming. Built with **Python**, **Click** and **Rich**.




## Features

- **Intuitive CLI:** Powered by [Click](https://click.palletsprojects.com/) for clean argument and option handling.
- **Beautiful Terminal UI:** Uses [Rich](https://rich.readthedocs.io/) for colored status messages, tables, and progress bars.




## Installation

Ensure you have Python 3.12 or higher installed.

    1. Clone the repository:
    git clone https://github.com/IchBinJannick/Renamer.git
    cd Renamer

    2. Create & activate a Virtual environment
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

    3. Install in Editable Mode:
    pip install -e .

## Usage

Display help and available options:

```bash
renamer --help
```

Example command:

```bash
renamer number ./my_photos --prefix "photo_"
```


##
Created by Jannick