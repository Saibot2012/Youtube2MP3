import yt_dlp

def download_mp3(url, output_folder):
    ydl_opts = {
        "format": "bestaudio/best",

        "outtmpl": f"{output_folder}/%(title)s.%(ext)s", 

        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def get_video_info(url):
    ydl_opts = {
        "quiet": True,
        "extract_flat": False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return{
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail")
    }
