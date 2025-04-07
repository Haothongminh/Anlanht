import subprocess

# URL của video YouTube
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Chạy lệnh yt-dlp và mpv để phát video
subprocess.run(['yt-dlp', '-o', '-', video_url, '|', 'mpv', '-'])
