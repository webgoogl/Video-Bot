# Main script
import asyncio
from utils.downloader import download_video
from utils.uploader import upload_video, create_post
from utils.monitor import monitor_directory

async def main():
    # Monitor videos directory and handle uploads
    await monitor_directory()

if __name__ == "__main__":
    asyncio.run(main())
