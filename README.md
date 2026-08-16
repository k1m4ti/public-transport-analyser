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

4. Running the Script Defined in `pyproject.toml`
```sh
poe download
```

## Project Structure
```text
.
├── README.md
├── data
│   └── downloads           # Directory to temporarily keep raw files
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

## Configuration

This project reads its configuration parameters from `pyproject.toml`. Under the `[tool.transport-analyser]` section, make sure you define the following settings:

```toml
[tool.transport-analyser]
bus_s_url = "https://gtfs.ztp.krakow.pl/GTFS_KRK_A.zip"     # source of schedule archive
bus_s_files =  [
    "trips.txt", 
    "stop_times.txt", 
    "routes.txt",
    "stops.txt"
]                                                           # list of files we want to extract
bus_s_dir = "data/downloads/bus_schedule"                   # directory we want to store above files
bus_u_url = "https://gtfs.ztp.krakow.pl/TripUpdates_A.pb"   # source of bus trip updates
bus_u_file =  "TripUpdates_A.pb"                            # the name of the file with updates
bus_u_dir = "data/downloads/bus_updates"                    # parent directory of above file
```