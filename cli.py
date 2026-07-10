import converter
import sys
import json

def display_commands():
    print('\n--------------------HELP--------------------\n')
    print('Download mp3/mp4 file for a YT vid:')
    print('download <filetype> <url>')
    print()
    print('Display info about YT vid:')
    print('info <url>')
    print()
    print('Get playlist videos:')
    print('playlist <url>')
    print()
    print('help')
    print('end')
    print('\n--------------------HELP--------------------\n')

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def main():

    if len(sys.argv) < 2:
        display_commands()
        return

    command = sys.argv[1]

    if command == "download":
        if len(sys.argv) < 4:
            print(json.dumps({
                "success": False,
                "error": "Faltan argumentos. Uso: download <mp3/mp4> <url>"
            }))
            return
        if not is_valid_url(sys.argv[3]):
            print(json.dumps({
                "success": False,
                "error": "URL no válida"
            }))
            return


    if command in ["info", "playlist"]:

        if len(sys.argv) < 3:
            print(json.dumps({
                "success": False,
                "error": "Falta la URL"
            }))
            return

        if not is_valid_url(sys.argv[2]):
            print(json.dumps({
                "success": False,
                "error": "URL no válida"
            }))
            return

    if command == "info":
        try:
            url = sys.argv[2]

            data = converter.info(url)

            print(json.dumps(data, ensure_ascii=False))

        except Exception as e:
            print(json.dumps({
                "success": False,
                "error": str(e)
            }))


    elif command == "download":
        try:
            filetype = sys.argv[2]
            url = sys.argv[3]

            if filetype == "mp4":
                result = converter.mp4download(url)

            elif filetype == "mp3":
                result = converter.mp3download(url)

            else:
                print(json.dumps({
                    "success": False,
                    "error": "Tipo de archivo no válido. Usa mp3 o mp4"
                }))
                return


            if result is True:
                print(json.dumps({
                    "success": True,
                    "data": "Descarga completada"
                }))

            else:
                print(json.dumps({
                    "success": False,
                    "error": result
                }))
            
        except Exception as e:
            print(json.dumps({
                "success": False,
                "error": str(e)
            }))

    elif command == "playlist":

        url = sys.argv[2]

        try:
            videos = converter.get_playlist(url)

            print(json.dumps({
                "success": True,
                "data": videos, 
                "errorData": None
            }))

        except Exception as e:
            print(json.dumps({
                "success": False,
                "data": "No data available",
                "errorData": str(e)
            }))


    elif command == "help":
        display_commands()


    else:
        print("Comando desconocido")
        display_commands()

if __name__ == "__main__":
    main()