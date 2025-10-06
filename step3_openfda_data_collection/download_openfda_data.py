import requests
import zipfile
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

SAVE_DIR = "openfda_drug_event_zips"
EXTRACT_DIR = os.path.join(SAVE_DIR, "unzipped")
DOWNLOAD_META_URL = "https://api.fda.gov/download.json"
MAX_WORKERS = 5


def download_and_extract(url, zip_path, json_path):
    try:
        # Download .zip
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Extract .json
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_DIR)

        os.remove(zip_path)

        return f"Downloaded and extracted: {os.path.basename(json_path)}"

    except Exception as e:
        return f"Failed: {os.path.basename(zip_path)} — {e}"


def main():
    os.makedirs(SAVE_DIR, exist_ok=True)
    os.makedirs(EXTRACT_DIR, exist_ok=True)
 
    print("Fetching metadata from OpenFDA...")
    try:
        response = requests.get(DOWNLOAD_META_URL)
        response.raise_for_status()
        meta = response.json()
        partitions = meta["results"]["drug"]["event"]["partitions"]
        print(f"Found {len(partitions)} drug event files.\n")
    except Exception as e:
        print(f"Failed to fetch metadata: {e}")
        return

    tasks = []
    for part in partitions:
        url = part["file"]
        filename = url.split("/")[-1]
        zip_path = os.path.join(SAVE_DIR, filename)
        json_filename = filename.replace(".zip", "")
        json_path = os.path.join(EXTRACT_DIR, json_filename)

        if os.path.exists(json_path):
            print(f"Already extracted: {json_filename}")
            continue

        tasks.append((url, zip_path, json_path))

    if not tasks:
        print("No new files to download.")
        return

    print(f"\nStarting with {MAX_WORKERS} threads...\n")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(download_and_extract, url, z, j) for url, z, j in tasks]
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
