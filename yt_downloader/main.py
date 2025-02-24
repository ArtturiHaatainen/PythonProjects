import tkinter
import customtkinter
from pytubefix import YouTube

def start_download():
    try:
        yt_link = link.get()    
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        print(f"Downloading {yt_object.title}...")
        video.download(output_path="C:/Users/Artturi/Downloads")
        print("Download completed")
    except Exception as e:
        print(f"Error: {e}")
        print("YouTube link may not be valid or there is a problem with the internet connection")

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



# Run app
app.mainloop()