from yt_dlp import YoutubeDL
import re
import os


#Function for getting MP4 progressive video files
def mp4download(url):
    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "restrictfilenames": True,
            "progress_hooks": [progress_hook],
            "no_warnings": True,
            "quiet": True,
            "noprogress": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return True
    except Exception as e:
        return str(e)

#MP3 file function
def mp3download(url):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "restrictfilenames": True,
            "progress_hooks": [progress_hook],
            "no_warnings": True,
            "quiet": True,
            "noprogress": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return True
    except Exception as e:
        return str(e)


#Display Video Info
def info(url):
    with YoutubeDL({
        "quiet": True,
        "no_warnings": True
    }) as ydl:

        info = ydl.extract_info(url, download=False)

    title = info.get("title") or "Vídeo sin título"

    return {
        "title": title,
        "channel": info["channel"],
        "views": info.get("view_count"),
        "date": info.get("upload_date"),
        "duration": info.get("duration")
    }
#Get playlist videos
def get_playlist(url):

    with YoutubeDL({
        "extract_flat": True,
        "quiet": True,
        "no_warnings": True
    }) as ydl:

        data = ydl.extract_info(url, download=False)

    videos = []

    for index, entry in enumerate(data["entries"], start=1):

        title = entry.get("title") or f"Vídeo sin título ({index})"
        video_url = entry.get("url") or ""

        videos.append({
            "title": title,
            "url": video_url
        })

    return videos

def progress_hook(data):
    pass

# def progress_hook(data):
#     if data["status"] == "downloading":
#
#         downloaded = data.get("_percent_str", "0%")
#
#        print({
#            "status": "downloading",
#            "percent": downloaded
#        })
#
#    elif data["status"] == "finished":
#
#        print({
#            "status": "finished",
#            "message": "Procesando archivo..."
#        })
