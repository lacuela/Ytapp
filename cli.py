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


def main():

    if len(sys.argv) < 2:
        display_commands()
        return

    command = sys.argv[1]


    if command == "info":

        url = sys.argv[2]

        data = converter.info(url)

        print(json.dumps(data))


    elif command == "download":

        filetype = sys.argv[2]
        url = sys.argv[3]
        mensaje = f"Descargando {filetype} de {url}"

        if filetype == "mp4":
            result = converter.mp4download(url)

        elif filetype == "mp3":
            result = converter.mp3download(url)

        else:
            mensaje = "Tipo de archivo no válido"
            return


        if result is True:
            mensaje = "Descarga completada"
            print(json.dumps({
                "success": True,
                "message": mensaje
            }))

        else:
            print(json.dumps({
                "success": False,
                "error": result
            }))

    elif command == "playlist":
        url = sys.argv[2]
        videos = converter.get_playlist(url)
        print(json.dumps(videos))


    elif command == "help":
        display_commands()


    else:
        print("Comando desconocido")
        display_commands()

if __name__ == "__main__":
    main()