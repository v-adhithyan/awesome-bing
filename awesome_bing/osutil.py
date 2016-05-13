import platform
import os

def get_os_name():
	return platform.system()

def check_and_make_directory(pic_dir):
	if not os.path.exists(pic_dir):
		print "Creating new directory ...\n"
		print "The path to new directory is: " + pic_dir
		os.makedirs(pic_dir)
	else:
		print "Directory exists"

def get_pic_directory():
	os_name = get_os_name().lower()
	pic_dir = ""
	bing_pics = os.path.sep + "Pictures" + os.path.sep + "bing"

	if(os_name == "darwin" or os_name == "linux"):
		if(os.environ.has_key("HOME")):
			pic_dir = os.environ.get("HOME")
			pic_dir = pic_dir  + bing_pics
	elif(os_name == "windows"):
		print "Windows"
	else:
		print "Unsupported os."

	check_and_make_directory(pic_dir)
	return pic_dir