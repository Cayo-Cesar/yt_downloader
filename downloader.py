import tkinter as tk
from pytube import YouTube
import os

# window = tk.Tk()
# window.title('Youtube Downloader')
# window.geometry('500x300')

url = input("Enter the url of the video: ")
yt = YouTube(url)
video_title = yt.title

print("Baixar: ")
print("1. MP3")
print("2. MP4")

option = int(input("Option: "))

if option == 1:
    print(f"Baixando MP3 do vídeo '{video_title}'...")
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_file = audio_stream.download(output_path=".", filename='audio_only')
    base, ext = os.path.splitext(audio_file)
    new_file = f"{video_title}.mp3"  # Usando o título do vídeo como nome do arquivo
    os.rename(audio_file, new_file)
    print("Download concluído!")

elif option == 2:
    print("Qualidade: ")
    print("1. 360p")
    print("2. 720p")
    print("3. 1080p")

    quality = int(input("Option: "))

    if quality == 1:
        print(f"Baixando MP4 em 360p do vídeo '{video_title}'...")
        yt.streams.filter(res="360p").first().download()
        new_file = f"{video_title}.mp4"  # Usando o título do vídeo como nome do arquivo
        os.rename(video_title + ".mp4", new_file)
        print("Download concluído!")

    elif quality == 2:
        print("Baixando MP4 em 720p do vídeo '{video_title}'...")
        yt.streams.filter(res="720p").first().download()
        new_file = f"{video_title}.mp4"
        os.rename(video_title + ".mp4", new_file)
        print("Download concluído!")

    elif quality == 3:
        print("Baixando MP4 em 1080p do vídeo '{video_title}'...")
        yt.streams.filter(res="1080p").first().download()
        new_file = f"{video_title}.mp4"
        os.rename(video_title + ".mp4", new_file)
        print("Download concluído!")

    else:
        print("Opção inválida!")

else:
    print("Opção inválida!")


#window.mainloop()