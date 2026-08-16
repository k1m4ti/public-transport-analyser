from config import APP_CONFIG
from pathlib import Path
import requests
import io
import zipfile


def download_schedule(url: str, files: list, save_path: Path) -> None:
    """Download a zip archive containing transit schedules and extract specific files.

    Args:
        url (str): The endpoint URL to fetch the zip file from.
        files list): A list of specific filenames to look for and extract from the archive.
        save_path (Path): The local directory where extracted files will be saved.
    """
    if not url:
        print("Error: url is missing in the configuration")
        return

    print(f"Downloading schedule from: {url}")
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Network error while downloading schedule: {e}")
        return

    try:
        zip_buffer = io.BytesIO(response.content)
        save_path.mkdir(exist_ok=True)

        with zipfile.ZipFile(zip_buffer, "r") as zf:
            for file in files:
                if file in zf.namelist():
                    file_bytes = zf.read(file)
                    destination = save_path / file
                    destination.write_bytes(file_bytes)
                    print(f"Successfully saved: {destination}")
                else:
                    print(f"Skipping (not found in zip): {file}")
    except zipfile.BadZipFile:
        print(f"Error: The downloaded file is not a valid zip archive.")
    except Exception as e:
        print(
            f"An unexpected error occured while processing schedule files: {e}")


def download_updates(url: str, file: str, save_path: Path) -> None:
    """Download an individual update file and save it locally.

    Args:
        url (str): The endpoint URL to fetch the file from.
        file (str): The name of the file being saved.
        save_path (Path): The local directory where the file will be saved.
    """
    if not url:
        print("Error: url is missing in the configuration")
        return

    print(f"Downloading updates from: {url}")

    save_path.mkdir(exist_ok=True)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        destination = Path(save_path) / file
        Path(destination).write_bytes(response.content)
        print(f"Successfully saved: {destination}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download update file '{file}': {e}")
        return


def main():
    """Load configuration parameters and execute the download tasks."""
    bus_s_url = APP_CONFIG.get("bus_s_url")
    bus_s_files = APP_CONFIG.get("bus_s_files")
    bus_s_dir = Path(APP_CONFIG.get("bus_s_dir"))

    bus_u_url = APP_CONFIG.get("bus_u_url")
    bus_u_file = APP_CONFIG.get("bus_u_file")
    bus_u_dir = Path(APP_CONFIG.get("bus_u_dir"))

    download_schedule(bus_s_url, bus_s_files, bus_s_dir)
    download_updates(bus_u_url, bus_u_file, bus_u_dir)


if __name__ == "__main__":
    main()
