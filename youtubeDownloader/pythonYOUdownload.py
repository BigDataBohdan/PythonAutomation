from pytube import YouTube
from sys import argv

link = argv[1]
YouTubes  = YouTube(link)
print("Title: ", YouTubes.title)
print("View: ", YouTubes.views)

ydube = YouTubes.streams.get_highest_resolution()

ydube.download('D:\PythonDev\PythonAutomation\youtubeDownloader')

