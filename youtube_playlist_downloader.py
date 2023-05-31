import os
import subprocess
import concurrent.futures


def download_video(video_id):
    subprocess.run(['youtube-dl', '--extract-audio', '--audio-format', 'mp3', '--output', f'temp/{video_id}.%(ext)s', f'https://www.youtube.com/watch?v={video_id}'])


def download_all_videos(playlist_url):
    # Create the 'temp' directory if it doesn't exist
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Get the total number of videos in the playlist
    result = subprocess.run(['youtube-dl', '--get-id', '--flat-playlist', playlist_url], capture_output=True, text=True)
    video_ids = result.stdout.strip().split('\n')

    # Download all videos in the playlist as MP3 files using parallel threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_video, video_ids)

    print('Download complete.')


# Replace 'PLAYLIST_URL' with the actual URL of the YouTube playlist
playlist_url = 'https://www.youtube.com/watch?v=m6Fh5wbA0_k&list=PLxhX9B5u13xSy0f3K7VBbHhVyQKAbGFFC'

download_all_videos(playlist_url)
