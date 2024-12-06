# Uploading functions
import requests
import os
from tqdm import tqdm

API_TOKEN = os.getenv("FLIC_TOKEN")
HEADERS = {"Flic-Token": API_TOKEN, "Content-Type": "application/json"}

def get_upload_url():
    url = "https://api.socialverseapp.com/posts/generate-upload-url"
    response = requests.post(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def upload_video(file_path, upload_url):
    with open(file_path, "rb") as f, tqdm(total=os.path.getsize(file_path), unit="B", unit_scale=True) as pbar:
        response = requests.put(upload_url, data=f, headers={"Content-Type": "video/mp4"})
        response.raise_for_status()
        pbar.update(os.path.getsize(file_path))
    print(f"Uploaded: {file_path}")

def create_post(title, hash_key, category_id):
    url = "https://api.socialverseapp.com/posts"
    body = {
        "title": title,
        "hash": hash_key,
        "is_available_in_public_feed": False,
        "category_id": category_id,
    }
    response = requests.post(url, headers=HEADERS, json=body)
    response.raise_for_status()
    print("Post created successfully!")
