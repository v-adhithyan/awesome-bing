import bing
import osutil

def help():
    return """** awesome-bing **\n
    Use awesome-bing with any of the following options:\n
    help - to know about the list of options available.\n
    getset - to get image of the day from bing and set as wallpaper.\n
    info - to get the story associated with the image of the day.\n
    For example type "awesome-bing info" without quotes the get today's image story from bing.\n"""

def info():
    bing.get_info()

def getset():
	fname = bing.download_image()
	print "Setting as wallpaper .."
	osutil.set_wallpaper(fname)

def pic_dir():
    return osutil.get_pic_directory()