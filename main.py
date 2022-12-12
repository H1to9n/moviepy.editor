import moviepy.editor
from pathlib import Path

def download_mp3(video_file):
    video_file = Path(video_file)
    video = moviepy.editor.VideoFileClip(f"{video_file}")
    audio = video.audio
    audio.write_audiofile(f"{video_file.stem}.mp3")

#video directory
download_mp3("")