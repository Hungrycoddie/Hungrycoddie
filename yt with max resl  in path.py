import pytube
url = input("Enter your Url: ")
path ="/Users/hungrycodie/Desktop"
pytube.YouTube(url).streams.get_highest_resolution().download(path)