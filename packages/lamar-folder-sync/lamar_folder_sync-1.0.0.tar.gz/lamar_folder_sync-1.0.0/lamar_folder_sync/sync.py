import requests
import os
import json
from .config import API_KEY

API_URL = "https://cmsprod.lamar.edu/api/v1/read"
CREATE_FOLDER_API_URL = "https://cmsprod.lamar.edu/api/v1/create"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def create_folder(parent_id, folder_name, site_id):
    create_payload = {
        "authentication": {"apiKey": API_KEY},
        "asset": {
            "folder": {
                "includeInStaleContent": True,
                "shouldBePublished": False,
                "shouldBeIndexed": False,
                "parentFolderId": parent_id,
                "siteId": site_id,
                "name": folder_name,
            }
        }
    }

    try:
        response = requests.post(CREATE_FOLDER_API_URL, headers=HEADERS, json=create_payload)
        response.raise_for_status()
        return response.json().get("createdAssetId")
    except requests.exceptions.RequestException as e:
        print(f"Error creating folder '{folder_name}': {e}")
        return None

def replicate_folders(source_folder_id, destination_parent_id):
    if source_folder_id == destination_parent_id:
        print("Source and destination folders are the same. Aborting to prevent infinite recursion.")
        return

    payload = {
        "authentication": {"apiKey": API_KEY},
        "identifier": {"type": "folder", "id": source_folder_id}
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching folder '{source_folder_id}': {e}")
        return

    if "asset" in data and "folder" in data["asset"]:
        source_folder = data["asset"]["folder"]
        subfolders = source_folder.get("children", [])

        for subfolder in subfolders:
            if subfolder["type"] == "folder" and "path" in subfolder:
                folder_name = subfolder["path"]["path"].split("/")[-1]
                site_id = subfolder["path"]["siteId"]
                new_folder_id = create_folder(destination_parent_id, folder_name, site_id)

                if new_folder_id:
                    print(f"Replicating subfolders of '{subfolder['id']}'")
                    replicate_folders(subfolder["id"], new_folder_id)
            else:
                print(f"Skipping folder due to missing required fields: {subfolder}")
