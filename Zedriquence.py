import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
from datetime import datetime

import webbrowser

def open_github(event):
    webbrowser.open_new("https://github.com/realzedrix/")

def video_to_images(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(output_folder, f"frame_{frame_count}.png"), frame)
        frame_count += 1
    cap.release()
    cv2.destroyAllWindows()

def browse_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.mpeg")])
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)

def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder)

def convert_video():
    video_path = video_entry.get()
    output_folder = os.path.join(output_entry.get(), f"Zedriquence {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}")
    if not os.path.isfile(video_path):
        result_label.config(text="Please select a video file", fg="red")
        return
    result_label.config(text="Converting...", fg="black")
    video_to_images(video_path, output_folder)
    result_label.config(text="Successful", fg="green")

def change_language(lang):
    if lang == "English":
        window.title("Zedriquence")
        video_label.config(text="Choose a video", font=("Rabar_021", 12))
        output_label.config(text="Output folder", font=("Rabar_021", 12))
        browse_video_button.config(text="Browse", font=("Rabar_021", 10))
        browse_output_button.config(text="Browse", font=("Rabar_021", 10))
        convert_button.config(text="Convert", font=("Rabar_021", 12))
        result_label.config(font=("Rabar_021", 12))
        copyright_label.config(text="© Zedriquence. All Rights Reserved.", font=("Rabar_021", 10))
        developer_label.config(text="Developed by Karden Karwan (Zedrix).", font=("Rabar_021", 10))
    elif lang == "Kurdish":
        window.title("Zedriquence")
        video_label.config(text="ڤیدیۆیەک هەڵبژێرە", font=("Rabar_021", 12))
        output_label.config(text="فۆڵدەر", font=("Rabar_021", 12))
        browse_video_button.config(text="هەڵبژاردن", font=("Rabar_021", 10))
        browse_output_button.config(text="هەڵبژاردن", font=("Rabar_021", 10))
        convert_button.config(text="دەستپێکردن", font=("Rabar_021", 12))
        result_label.config(font=("Rabar_021", 12))
        copyright_label.config(text="© Zedriquence. All Rights Reserved.", font=("Rabar_021", 10))
        developer_label.config(text="Developed by Karden Karwan (Zedrix).", font=("Rabar_021", 10))

def show_language_menu():
    menubar = tk.Menu(window)
    language_menu = tk.Menu(menubar, tearoff=0)
    language_menu.add_command(label="English", command=lambda: change_language("English"))
    language_menu.add_command(label="Kurdish", command=lambda: change_language("Kurdish"))
    menubar.add_cascade(label="Language (English/Kurdish)", menu=language_menu)

    window.config(menu=menubar)

window = tk.Tk()
window.title("Zedriquence")
window.geometry("500x500")
window.configure(bg="#2c3e50")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.resizable(False, False)

logo_path = "ZedriquenceLogo.png"
logo_img = Image.open(logo_path)
logo_img = logo_img.resize((100, 100), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(window, image=logo_img, bg="#2c3e50")
logo_label.grid(row=0, column=0, pady=10)

show_language_menu()

input_frame = tk.Frame(window, bg="#2c3e50")
input_frame.grid(row=1, column=0, pady=10, padx=20, sticky="ew")
input_frame.grid_columnconfigure(1, weight=1)

video_label = tk.Label(input_frame, text="Choose a video", font=("Rabar_021", 12), bg="#2c3e50", fg="white", justify='right')
video_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")

video_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
video_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

browse_video_button = tk.Button(input_frame, text="Browse", command=browse_video, bg="#1abc9c", fg="white", font=("Rabar_021", 10), relief="flat", justify='right')
browse_video_button.grid(row=0, column=0, padx=10, pady=5)

output_label = tk.Label(input_frame, text="Output folder", font=("Rabar_021", 12), bg="#2c3e50", fg="white")
output_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")

output_entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
output_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

browse_output_button = tk.Button(input_frame, text="Browse", command=browse_output_folder, bg="#1abc9c", fg="white", font=("Rabar_021", 10), relief="flat")
browse_output_button.grid(row=1, column=0, padx=10, pady=5)

convert_button = tk.Button(window, text="Convert", command=convert_video, bg="#e74c3c", fg="white", font=("Rabar_021", 12), relief="flat")
convert_button.grid(row=2, column=0, pady=5)

result_label = tk.Label(window, text="", font=("Rabar_021", 12), bg="#2c3e50", fg="white")
result_label.grid(row=3, column=0, pady=15)

copyright_label = tk.Label(window, text="© Zedriquence. All Rights Reserved.", font=("Rabar_021", 10), bg="#2c3e50", fg="white")
copyright_label.grid(row=4, column=0)

developer_label = tk.Label(window, text="Developed by Karden Karwan (Zedrix).", font=("Rabar_021", 10), bg="#2c3e50", fg="cyan")
developer_label.grid(row=5, column=0, pady=15)

copyright_label.bind("<Button-1>", open_github)

window.mainloop()
