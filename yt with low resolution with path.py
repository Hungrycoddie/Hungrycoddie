
import pytube
from pytube import YouTube
def downloadVideo():
	myURL = input("Please paste in the URL of the video you want to download: ")
    
	if type(myURL) == str:
		yt = YouTube(myURL)
		stream = myURL.streams.get_highest_resolution()
		location = input("Please specify the directory you want to save the video to: ")
		if type(location) == str:
			myURL.download(location)
			print("Video downloaded successfuly")
		else: 
			print("Please enter a vaid location")
			downloadVideo()
	else:
		print("Please enter a valid URL")
		downloadVideo()
        
downloadVideo()
