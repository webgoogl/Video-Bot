 # Downloading functions
import requests
from tqdm import tqdm

def download_video(platform, video_url, save_path):
    response = requests.get(video_url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    with open(save_path, "wb") as f, tqdm(total=total_size, unit="B", unit_scale=True) as pbar:
        for data in response.iter_content(chunk_size=1024):
            f.write(data)
            pbar.update(len(data))
    print(f"Downloaded: {save_path}")
