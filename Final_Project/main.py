from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=fJ9rUzIMcZQ&pp=ygUFcXVlZW4%3D")

# print(yt.title)
# print(yt.thumbnail_url)
# for item in yt.streams:
#     print(item)
# print()
# for item in yt.streams.filter(only_audio=True, file_extension="mp3"):
#     print(item)
stream = yt.streams.get_by_itag(251)
print(stream)
# stream.download(filename="Never Forget - Kessoku Band.mp3")
