import datetime
import osutil
import os

fname = osutil.get_home_directory() + os.path.sep + ".awesome-bing.txt"

def today_set():
	today = str(datetime.date.today())

	if not osutil.file_exists(fname):
		return False

	if get_todays_info().find(today) != -1:
		return True

	return False

def set_today_and_info(content):
	file = open(fname, "w")
	file.write(content)
	file.close()

def get_todays_info():
	file = open(fname, "r")
	content = file.read()
	file.close()

	return str(content)

def get_info():
	today = str(datetime.date.today())
	return get_todays_info().replace(today, "")