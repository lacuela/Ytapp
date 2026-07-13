from yt_dlp import YoutubeDL
import re
import os


#Function for getting MP4 progressive video files
def mp4download(url, folder=None):
    try:

        if folder:
            output_folder = os.path.join("downloads", folder)
            os.makedirs(output_folder, exist_ok=True)
            outtmpl = os.path.join(output_folder, "%(title)s.%(ext)s")
        else:
            os.makedirs("downloads", exist_ok=True)
            outtmpl = os.path.join("downloads", "%(title)s.%(ext)s")

        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "merge_output_format": "mp4",
            "outtmpl": outtmpl,
            "restrictfilenames": True,
            "progress_hooks": [progress_hook],
            "no_warnings": True,
            "quiet": True,
            "noprogress": True,
            "ignoreerrors": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return True

    except Exception as e:
        return str(e)

#MP3 file function
def mp3download(url, folder=None):
    try:
        if folder:
            output_folder = os.path.join("downloads", folder)
            os.makedirs(output_folder, exist_ok=True)
            outtmpl = os.path.join(output_folder, "%(title)s.%(ext)s")
        else:
            os.makedirs("downloads", exist_ok=True)
            outtmpl = os.path.join("downloads", "%(title)s.%(ext)s")

        ydl_opts = {
            "format": "bestaudio/best",
            "writethumbnail": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {
                "key": "FFmpegMetadata",
            },
            {
                "key": "EmbedThumbnail",
            }],
            "outtmpl": outtmpl,
            "restrictfilenames": True,
            "progress_hooks": [progress_hook],
            "no_warnings": True,
            "quiet": True,
            "noprogress": True,
            "ignoreerrors": True,
            "embed_metadata": True
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
        playlist_title = data.get("title", "Playlist")
        playlist_title = re.sub(r'[<>:"/\\|?*]', "_", playlist_title)

    videos = []

    for index, entry in enumerate(data["entries"], start=1):

        title = entry.get("title") or f"Vídeo sin título ({index})"
        video_url = entry.get("url") or ""

        videos.append({
            "title": title,
            "url": video_url
        })

    return {
        "playlist_title": playlist_title,
        "videos": videos
    }

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
