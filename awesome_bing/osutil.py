import platform
import os

def get_os_name():
	return platform.system()

def check_and_make_directory(pic_dir):
	if not os.path.exists(pic_dir):
		if pic_dir.find("-") != -1:	
			print "Creating new directory to store bing images for the current month...\n"
			print "The path to new directory is: " + pic_dir
			
		os.makedirs(pic_dir)

def file_exists(fname):
	return os.path.isfile(fname)

def get_home_directory():
	if(os.environ.has_key("HOME")):
		return os.environ.get("HOME")

def get_pic_directory():
	os_name = get_os_name().lower()
	pic_dir = ""
	bing_pics = os.path.sep + "Pictures" + os.path.sep + "bing"

	if(os_name == "darwin" or os_name == "linux"):
			pic_dir = get_home_directory()
			pic_dir = pic_dir  + bing_pics
	elif(os_name == "windows"):
		print "Windows"
	else:
		print "Unsupported os."

	check_and_make_directory(pic_dir)
	return pic_dir

def set_wallpaper(fname):
	os_name = get_os_name().lower()

	if os_name == "darwin":
		os.system('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "' + fname + '"\'')
	else:
		print "Currently Unsupported."