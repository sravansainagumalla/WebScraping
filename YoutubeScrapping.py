from pytube import YouTube


link = 'https://youtu.be/kn8ZuOCn6r0'

print(link)

yt = YouTube(link)


print("Title:", yt.title)

print("Views:", yt.views)

print("Duration:", yt.duration)

print("Credits:", yt.credits)

print("Description :", yt.description)

