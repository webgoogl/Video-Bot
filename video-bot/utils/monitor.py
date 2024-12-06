# Directory monitoring
import asyncio
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils.uploader import get_upload_url, upload_video, create_post

class VideoHandler(FileSystemEventHandler):
    async def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".mp4"):
            return

        file_path = event.src_path
        print(f"New file detected: {file_path}")

        try:
            # Step 1: Get upload URL
            data = get_upload_url()
            upload_url = data["upload_url"]
            hash_key = data["hash"]

            # Step 2: Upload video
            upload_video(file_path, upload_url)

            # Step 3: Create post
            await asyncio.sleep(1)  # Simulate async behavior
            create_post("Sample Title", hash_key, 1)

            # Step 4: Delete file locally
            os.remove(file_path)
            print(f"File deleted: {file_path}")

        except Exception as e:
            print(f"Error handling file {file_path}: {e}")

async def monitor_directory():
    event_handler = VideoHandler()
    observer = Observer()
    path = "./videos"
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
import os

async def monitor_directory():
    path = os.path.join(os.getcwd(), "videos")  # Use absolute path
    print(f"Monitoring directory: {path}")

    if not os.path.exists(path):
        print(f"Directory does not exist: {path}. Creating it.")
        os.makedirs(path)
    
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
