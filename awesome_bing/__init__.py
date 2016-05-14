import bing
import osutil

def help():
    return """** awesome-bing **\n
    Use awesome-bing with any of the following options:\n        
    * help - to know about the list of options available.\n
    * info - to get the story associated with the image of the day.\n
    * set - to get image of the day from bing and set as wallpaper.\n
    ****For example type "awesome-bing info" without quotes the get today's image story from bing. \n"""

def info():
    bing.info()

def set():
	fname = bing.download_image()
	print "Setting the downloaded image as wallpaper .."
	osutil.set_wallpaper(fname)
