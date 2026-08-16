## Getting Started

Follow these steps to set up your local development environment and run the project.

### Prerequisites

Make sure you have **Micromamba** (or Conda) installed on your system.

1. Create the Micromamba Environment
Run the following command in your terminal to provision the local environment (.venv) with Python and Perl:
```sh
micromamba create -p .venv -f environment.yml -y
```

2. Activate the Environment
```sh
micromamba activate .venv
```

3. Install the Project in Editable Mode
Install the package and its dependencies locally:
```sh
pip install -e .
```

4. Running the Program
```sh
python src/main.py
```

## Project Structure
```text
.
├── README.md
├── environment.yml         # Micromamba setup (Python + Perl)
├── perl                    # Perl codebase
│   ├── lib                 # Custom Perl modules (.pm)
│   └── scripts             # Executable Perl scripts (.pl)
├── pyproject.toml          # Python package metadata
├── src                     # Python codebase
│   ├── downloader
│   └── main.py
└── tests
    ├── perl                # Perl tests (using Test::More & prove)
    └── python              # Python tests (using pytest)
```