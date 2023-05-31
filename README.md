# YouTube Playlist Downloader

This Python script allows you to download all the videos in a YouTube playlist as MP3 files. It utilizes the `youtube-dl` library to extract audio from the videos and save them in the MP3 format.

## Features

- Downloads all videos in a YouTube playlist as MP3 files
- Saves the downloaded files in a designated directory
- Supports parallel downloading for faster execution (using threads)

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:

`pip install -r requirements.txt`

## Usage

1. Clone this repository or download the `youtube_playlist_downloader.py` file.
2. Run the script by executing the following command:

`python youtube_playlist_downloader.py`

3. Enter the URL of the YouTube playlist you want to download when prompted.

**Note:** Make sure the playlist is publicly accessible and does not contain any private or restricted videos.

4. The script will start downloading the videos in the playlist as MP3 files. The downloaded files will be saved in the `temp` directory.

5. Once the download is complete, you can find the downloaded MP3 files in the `temp` directory.

## Dependencies

- [youtube-dl](https://github.com/ytdl-org/youtube-dl): A command-line program to download videos from YouTube and other sites.

## Notes

- The script relies on the `youtube-dl` library for downloading videos. Make sure you have it installed and accessible from the command line.
- Be aware of the terms of service and any legal restrictions when downloading videos from YouTube.
- This script is provided as-is and may not work correctly with certain edge cases or changes in the YouTube API.

## License

This project is licensed under the [MIT License](LICENSE).
