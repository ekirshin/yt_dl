#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 13:03:18 2026

@author: ek
"""

import yt_dlp
import os

# ---------------------------------------------------------
# USER SETTINGS
# ---------------------------------------------------------

# DOWNLOAD_FORMAT:
#   Available audio codecs yt-dlp can extract via ffmpeg:
#   "mp3", "m4a", "aac", "flac", "wav", "opus", "vorbis"
DOWNLOAD_FORMAT = "flac"

# URL list
# Replace <YOUTUBE_ID> with YT video ID in the URL
URLS = ['https://www.youtube.com/watch?v=6GxAS-mnXwo',
        'https://www.youtube.com/watch?v=G9qCqN5blxo' ]

# ---------------------------------------------------------
# CREATE OUTPUT FOLDER
# ---------------------------------------------------------

output_folder = os.path.expanduser(f"~/yt_dl/{DOWNLOAD_FORMAT}")
os.makedirs(output_folder, exist_ok=True)

# ---------------------------------------------------------
# YT-DLP OPTIONS
# ---------------------------------------------------------

ydl_opts = {
    # Download best audio available
    'format': 'bestaudio/best',

    # Save path: ./<format>/<song_name>.<format_extension>
    'outtmpl': os.path.join(output_folder, "%(title)s.%(ext)s"),

    # Extract audio using ffmpeg
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': DOWNLOAD_FORMAT,
            'preferredquality': '0',  # best quality for mp3; ignored for lossless
        }
    ],
}

# ---------------------------------------------------------
# RUN DOWNLOAD
# ---------------------------------------------------------

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
