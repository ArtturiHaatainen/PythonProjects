import tkinter
import customtkinter
from pytubefix import YouTube
from pathlib import Path

def start_download():
    try:
        yt_link = link.get()    
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()

        title.configure(text=yt_object.title)
        dl_finished.configure(text="")
        dl_folder = Path.home() / "Downloads"
        video.download(dl_folder)
        dl_finished.configure(text="Download finished!")
    except Exception as e:
        dl_finished.configure(text="YouTube link may not be valid or there is a problem with the internet connection", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    dl_progressbarp.configure(text=f"{round(percentage)}%")
    dl_progressbarp.update()

    dl_progressbar.set(percentage / 100)
    dl_progressbar.update()
# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame
app = customtkinter.CTk()
app.geometry("800x600")
app.title("YouTube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert link", font=("Arial", 20))
title.pack(padx=20, pady=20)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=50, font=("Arial", 15), textvariable = url_var)
link.pack(padx=20, pady=20)

dl_button = customtkinter.CTkButton(app, text="Download", font=("Arial", 15), command=start_download)
dl_button.pack(padx=20, pady=20)

dl_progressbar = customtkinter.CTkProgressBar(app, width=400)
dl_progressbar.set(0)
dl_progressbar.pack(padx=20, pady=20)

dl_progressbarp = customtkinter.CTkLabel(app, text="0%", font=("Arial", 15))
dl_progressbarp.pack(padx=20, pady=20)

dl_finished = customtkinter.CTkLabel(app, text="", font=("Arial", 15))
dl_finished.pack(padx=20, pady=20)
# Run app
app.mainloop()