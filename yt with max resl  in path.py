#import library 
import pytube
#input your url 
url = input("Enter your Url: ")
#locate your path in which you want to download 
path ="Your path here"
#call the functions
pytube.YouTube(url).streams.get_highest_resolution().download(path)
