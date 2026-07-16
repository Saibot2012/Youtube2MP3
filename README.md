# 🎵 Convo-Audio

A simple and modern desktop application built with Python that converts YouTube videos into high-quality MP3 audio files.

Designed with a clean graphical interface using CustomTkinter, Convo-Audio allows users to paste a YouTube link, choose an output folder, and download the audio with just a few clicks.

---

## ✨ Features

- 🎵 Convert YouTube videos to MP3
- 🖥️ Modern desktop interface built with CustomTkinter
- 📁 Choose your own download location
- ⚡ Fast conversion using yt-dlp
- 💾 Export audio in MP3 format
- 📦 Packaged as a standalone Windows executable

---

## 🛠️ Technologies Used

- Python 3.11
- CustomTkinter
- yt-dlp
- FFmpeg
- PyInstaller

---

## 📷 Screenshots

### Main Window

> ![Main window](assets\Screenshot 2026-07-16 232009.png)



## 🚀 Installation

### Option 1 – Download the executable

Download the latest release and run:

```
Convo-Audio.exe
```

No Python installation is required.

### Option 2 – Run from source

Clone the repository:

```bash
git clone https://github.com/Saibot2012/Youtube2MP3.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

This application requires FFmpeg to be installed and available in your system PATH. 

Run the application:

```bash
python main.py
```

---

## 📂 Project Structure

```
Convo-Audio/
│
├── assets/
├── downloader.py
├── gui.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

- Preview video information before downloading
- Download playlists
- Download progress bar
- Audio quality selection
- Automatic FFmpeg installation
- Improved error handling

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by GK as a personal Python project to learn desktop GUI development, Python packaging, and working with external libraries.