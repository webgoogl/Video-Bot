# Video-Bot
A Python-based bot that searches, downloads, and uploads videos from social media platforms like Instagram, TikTok, and Reddit, and uploads them to a server using provided APIs.
Table of Contents
Overview
Features
Installation
Usage
Project Structure
Environment Variables
Testing
FAQ
Contributing
License
Overview
This bot automates the process of downloading videos from social media platforms and uploading them to the Empowerverse server. It features directory monitoring for new videos and asynchronous uploads for better performance.

Features
Download videos from Instagram, TikTok, and Reddit.
Automatically monitor a directory for new .mp4 files.
Upload videos to a server using pre-signed URLs.
Create posts using an API with metadata like titles and categories.
Auto-delete local files after successful uploads.
Robust error handling and progress visualization.
Installation
Prerequisites
Install Python 3.9+.
Install Git for cloning the repository (optional).
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/video-bot.git
cd video-bot
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Create a .env file for environment variables:
plaintext
Copy code
FLIC_TOKEN=<your_api_token>
Usage
Run the Bot
Ensure the /videos directory exists in the project root.
Start the bot:
bash
Copy code
python main.py
Add .mp4 files to the /videos directory to trigger the upload process.
Expected Workflow
The bot monitors the /videos directory.
When a new .mp4 file is added:
It retrieves a pre-signed upload URL.
Uploads the video to the server.
Creates a post using the provided API.
Deletes the local file after successful upload.
Project Structure
plaintext
Copy code
video-bot/
├── main.py                # Main script
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
├── utils/                 # Utility scripts
│   ├── downloader.py      # Downloading functions
│   ├── uploader.py        # Uploading functions
│   ├── monitor.py         # Directory monitoring
└── README.md              # Documentation
Environment Variables
Create a .env file in the root directory with the following keys:

plaintext
Copy code
FLIC_TOKEN=<your_api_token>
FLIC_TOKEN: Your API token for authentication with Empowerverse.
Testing
Add test .mp4 files to the /videos directory.
Check logs for successful uploads and post creation.
Verify uploaded videos in the Empowerverse app under the "Super Feed" category.
FAQ
Q: How do I handle API token issues?
Ensure the correct token is added to the .env file.

Q: What happens if a video upload fails?
The bot logs the error and skips the file. You can retry by re-adding the file.

Q: Can I monitor a different directory?
Yes, update the path in utils/monitor.py to the desired directory.

Contributing
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-name
Commit changes and push the branch.
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

