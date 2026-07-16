import customtkinter as ctk
from tkinter import filedialog
from downloader import download_mp3, get_video_info

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.output_folder = ""

        self.title("Convo-Audio")
        self.geometry("600x450")
        self.resizable(True, True)


        #Title

        self.title_label = ctk.CTkLabel(
            self,
            text="Youtube To MP3 Converter",
            font=("Arial", 24, "bold")
        )

        self.title_label.pack(pady=(20,20))

        #URL Label
        self.url_label = ctk.CTkLabel(
            self,
            text="Youtube URL"
        )
        self.url_label.pack(anchor="w", padx=40)

        self.url_entry = ctk.CTkEntry(
            self,
            width=520
        )
        self.url_entry.pack(pady=(5,20))

        #Output Folder Label
        self.folder_label = ctk.CTkLabel(
            self,
            text="Output Folder"
        )
        self.folder_label.pack(anchor="w", padx=40)

        #Frame
        self.folder_frame = ctk.CTkFrame(self, fg_color = "transparent")
        self.folder_frame.pack(pady=(5,20))

        #Folder Entry
        self.folder_entry = ctk.CTkEntry(
            self.folder_frame,
            width=400
        )
        self.folder_entry.pack(side="left", padx=(0.10))

        #Browse Button
        self.browse_button = ctk.CTkButton(
            self.folder_frame,
            text="Browse",
            width=90,
            command=self.select_folder
        )
        self.browse_button.pack(side="left")

        #Convert Button
        self.convert_button = ctk.CTkButton(
            self,
            text="Convert",
            command=self.convert
        )
        self.convert_button.pack(pady=10)

        self.preview_button = ctk.CTkButton(
            self,
            text="Preview",
            command=self.preview_video
        )
        self.preview_button.pack()
        self.video_title = ctk.CTkLabel(
            self,
            text="Title: -"
        )
        self.video_title.pack(pady=(10, 0))

        self.video_author = ctk.CTkLabel(
            self,
            text="Channel: -"
        )
        self.video_author.pack()

        self.video_duration = ctk.CTkLabel(
            self,
            text="Duration: -"
        )
        self.video_duration.pack()
        self.status = ctk.CTkLabel(
            self,
            text="Status: Waiting"
        )
        self.status.pack()

    def select_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.output_folder = folder
            self.folder_entry.delete(0, "end")
            self.folder_entry.insert(0, folder)

    def convert(self):
        url = self.url_entry.get()

        if not url:
            self.status.configure(text="Status: Please enter a URL.")
            return

        if not self.output_folder:
            self.status.configure(text="Status: Please select a folder.")
            return

        self.status.configure(text="Status: Downloading...")

        try:
            download_mp3(url, self.output_folder)
            self.status.configure(text="Status: Complete!")
        except Exception as e:
            self.status.configure(text=f"Status: Error")
            print(e)
    def format_duration(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02d}"
    
    def preview_video(self):
        url = self.url_entry.get()

        if not url:
            self.status.configure(text="Please enter a URL.")
            return

        try:
            info = get_video_info(url)

            self.video_title.configure(text=f"Title: {info['title']}")
            self.video_author.configure(text=f"Channel: {info['uploader']}")
            self.video_duration.configure(
                text=f"Duration: {self.format_duration(info['duration'])}"
            )

            self.status.configure(text="Video loaded.")

        except Exception as e:
            self.status.configure(text="Invalid URL.")
            print(e)


