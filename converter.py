from yt_dlp import YoutubeDL
import re
import os


#Function for getting MP4 progressive video files
def mp4download(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Descarga completada.")

#MP3 file function
def mp3download(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Audio descargado.")


#Display Video Info
def info(url):
    with YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)

    print(f"Título: {info['title']}")
    print(f"Canal: {info['channel']}")
    print(f"Visualizaciones: {info['view_count']}")
    print(f"Fecha: {info['upload_date']}")
    print(f"Duración: {info['duration']} segundos")

def display_commands():
    # Displays all possible commands and their use cases 
    print('\n--------------------HELP--------------------\n')
    print('Download mp3/mp4 file for a YT vid: download <filetype> <url>')
    print('Display info about YT vid: display info <url>')
    print('help: Provide info about commands, you just did it!')
    print('end: Quits the app')
    print('\n--------------------HELP--------------------\n')

# Boilerplate
if __name__ == '__main__':
    # Runs a loop, app ends when broken away from this function
    while True:
        # Get User input
        user_input = input('YtApp: ')
        # Separate input command into individual words, stored as a list
        command_word_arr = user_input.split()

        # Validate appropriate command length
        if len(command_word_arr) > 3 or len(command_word_arr) < 1:
            print("Invalid command length, use the command 'help' for assistance")
            continue

        # Check for help and quit commands
        elif len(command_word_arr) == 1:
            if user_input == 'help':
                display_commands() # Displays all possible commands and their uses
            elif user_input == 'end':
                break # Quits app
            else:
                print("Invalid one word command, use the command 'help' for assistance")
                continue
        elif command_word_arr[-1].startswith("http"): # Checks whether a YT url has been entered
            url = command_word_arr[-1]
            if command_word_arr[0] == 'download': # Download a new yt vid
                if command_word_arr[1].lower() == 'mp3':
                    mp3download(url) # Audio
                elif command_word_arr[1].lower() == 'mp4':
                    mp4download(url) # Video
                else:
                    print("Invalid filetype, use the command 'help' for assistance")
                    continue
            elif command_word_arr[0] == 'display' and command_word_arr[1] == 'info':
                info(url) # Display YT vid info
            else:
                print("Invalid yt vid command, use the command 'help' for assistance")
                continue
        else:
            print("Invalid command, use the command 'help' for assistance")
            continue