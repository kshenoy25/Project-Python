from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from urllib.request import build_opener, install_opener
import ssl

# Ensure proper SSL context
ssl._create_default_https_context = ssl._create_unverified_context

# Set custom User-Agent header
opener = build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")]
install_opener(opener)

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        # Get the highest resolution progressive stream
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        if stream:
            stream.download(output_path=save_path)
            print("Video downloaded successfully!")
        else:
            print("No suitable streams found for download.")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    video_url = input("Please enter the video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Starting download...")
        download_video(video_url, save_dir)
    else:
        print("No save location selected.")