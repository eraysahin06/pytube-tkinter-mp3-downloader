import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os

def download_audio():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        output_path = stream.download(output_path=download_path.get())
        base, ext = os.path.splitext(output_path)
        new_file = base + '.mp3'
        os.rename(output_path, new_file)
        status_label.config(text='Download completed!', fg='green')
    except Exception as e:
        status_label.config(text=f'Error: {e}', fg='red')

def browse_directory():
    directory = filedialog.askdirectory()
    download_path.delete(0, tk.END)
    download_path.insert(0, directory)

# Create the main window
root = tk.Tk()
root.title('YouTube MP3 Downloader')

# URL entry
url_label = tk.Label(root, text='Enter YouTube URL:')
url_label.pack(pady=(10, 0))
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Download path entry
path_label = tk.Label(root, text='Download Path:')
path_label.pack(pady=(10, 0))
download_path = tk.Entry(root, width=40)
download_path.pack(pady=5, side=tk.LEFT)
download_path.insert(0, os.getcwd())

# Browse button
browse_button = tk.Button(root, text='Browse', command=browse_directory)
browse_button.pack(pady=5, side=tk.RIGHT)

# Download button
download_button = tk.Button(root, text='Download', command=download_audio)
download_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text='', font=('Arial', 12))
status_label.pack(pady=10)

# Run the application
root.mainloop()
