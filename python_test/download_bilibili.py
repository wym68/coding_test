import os
import sys

def download_video(url):
    os.system("bilibili-download " + url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_video.py URL")
        sys.exit(1)
    download_video(sys.argv[1])

