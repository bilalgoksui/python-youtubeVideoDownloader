import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    selected_resolution = resolution_var.get()
    selected_format = format_var.get()

    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(res=selected_resolution, file_extension=selected_format).first()

        file_path = filedialog.asksaveasfilename(defaultextension=selected_format, filetypes=[(f"{selected_format.upper()} Files", f"*.{selected_format}")])

        if file_path:
            video_stream.download(output_path=file_path)
            status_label.config(text="İndirme başarılı.")
        else:
            status_label.config(text="İndirme iptal edildi.")
    except Exception as e:
        status_label.config(text=f"Hata: {e}")

window = tk.Tk()
window.geometry("300x250")
window.title("YouTube Downloader")

url_label = tk.Label(text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry()
url_entry.pack()

resolution_label = tk.Label(text="Çözünürlük:")
resolution_label.pack()
resolutions = ["720p", "480p", "360p"]
resolution_var = tk.StringVar()
resolution_var.set(resolutions[0])
resolution_dropdown = tk.OptionMenu(window, resolution_var, *resolutions)
resolution_dropdown.pack()

format_label = tk.Label(text="Format:")
format_label.pack()
formats = ["mp4", "mp3"]
format_var = tk.StringVar()
format_var.set(formats[0])
format_dropdown = tk.OptionMenu(window, format_var, *formats)
format_dropdown.pack()

download_button = tk.Button(text="İndir", command=download_video)
download_button.pack()

status_label = tk.Label(text="")
status_label.pack()

window.mainloop()
