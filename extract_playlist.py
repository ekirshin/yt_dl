#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 13:11:26 2026

@author: ek
"""

from yt_dlp import YoutubeDL
import os

# -----------------------------
# Customize these two variables
# -----------------------------

# DOWNLOAD_FORMAT:
#   Available audio codecs yt-dlp can extract via ffmpeg:
#   "mp3", "m4a", "aac", "flac", "wav", "opus", "vorbis"
DOWNLOAD_FORMAT = "flac"

# Flag to control re-downloading existing tracks
# Set to True to skip downloading tracks already in the folder (update with new only)
# Set to False to re-download and overwrite existing tracks
UPDATE_ONLY = True

# Replace <YOUTUBE_PL_ID> with YT video ID in the URL
# Note: <YOUTUBE_ID> - one of tracks IDs from the playlist
# Note: the playlist needs to be Public to download all the tracks from the playlist
playlist_url = "https://www.youtube.com/watch?v=3eRHuwqYizA&list=PLqX_LtipSXx_UiWiNClirBiIdEkAedR3t"


# Folder where audio files will be saved
playlist_name = "Rock_Metal_AI" # change this
download_folder = os.path.expanduser(f"/media/ek/EK_BACKUP/Music/ROCK_METAL_AI/{playlist_name}/{DOWNLOAD_FORMAT}") 

# Create folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# -----------------------------
# yt-dlp options
# -----------------------------

ydl_opts = {
    "format": "bestaudio/best",          # highest quality audio stream
    "extractaudio": True,
    "audioformat": "mp3",                # or "flac", "wav", "m4a"
    # Save path: ./<format>/<song_name>.<format_extension>
    'outtmpl': os.path.join(download_folder, "%(title)s.%(ext)s"),
    "ignoreerrors": True,
    "noplaylist": False, # Force full playlist download
    "continuedl": True,
    "nooverwrites": UPDATE_ONLY,
    "postprocessors": [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': DOWNLOAD_FORMAT,
            'preferredquality': '0',  # best quality for mp3; ignored for lossless
        }
    ],
}

# -----------------------------
# Download
# -----------------------------

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
