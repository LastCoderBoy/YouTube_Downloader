from pytube import YouTube
url = 'https://youtu.be/eGaImwD8fPQ' #paste the link of video that you want to download
yt = YouTube(url)
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")

