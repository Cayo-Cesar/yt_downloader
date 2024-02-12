#Autor: Cayo Cesar

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
from pytube import YouTube
from tqdm import tqdm
import os

def downloader_mp3():
    url = entry.get()
    yt = YouTube(url)
    video_title = yt.title

    save_path = filedialog.askdirectory()
    if save_path:
        print(f"Baixando MP3 do vídeo '{video_title}'...")
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        audio_file = audio_stream.download(output_path=save_path, filename='audio_only')
        base, ext = os.path.splitext(audio_file)
        new_file = f"{video_title}.mp3"  # Usando o título do vídeo como nome do arquivo
        os.rename(audio_file, os.path.join(save_path, new_file))
        messagebox.showinfo("Download Concluído", "Download do MP3 concluído!")

def downloader_mp4():
    url = entry.get()
    yt = YouTube(url)
    video_title = yt.title

    save_path = filedialog.askdirectory()
    if save_path:
        print(f"Baixando em MP4 do vídeo '{video_title}'...")
        yt.streams.filter(res="720p").first().download(output_path=save_path)
        new_file = f"{video_title}.mp4"
        os.rename(os.path.join(save_path, video_title + ".mp4"), os.path.join(save_path, new_file))
        messagebox.showinfo("Download Concluído", "Download do MP4 concluído!")

window = tk.Tk()
window.title('Youtube Downloader')
window.geometry('500x200')

label = tk.Label(window, text='Youtube Downloader', font=("Comic Sans MS", 20, "bold"))
label.pack()

entry = tk.Entry(window, width=50, font=('Arial', 14))
entry.pack()

button = tk.Button(window, text='Download MP3', command=downloader_mp3, font=("Comic Sans MS", 10, "bold"))
button.pack()

button2 = tk.Button(window, text='Download MP4', command=downloader_mp4, font=("Comic Sans MS", 10, "bold"))
button2.pack()

window.mainloop()
