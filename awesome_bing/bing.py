import os
import osutil
import re
from selenium import webdriver
import time
import urllib
import datetime
import awesomeutil

try_later = "Unknown error occured. Please try again after sometime."
bing = "http://www.bing.com"

def click_element(driver, element_name):

	try:
		element = driver.find_element_by_xpath(element_name)
		element.click()
		return True
	except:
		print try_later
		driver.quit()
		raise
		return False


def download_image():
	try:
		if not awesomeutil.today_set():
			driver = webdriver.Firefox()
			driver.get(bing)

			bg_div = driver.find_element_by_xpath("//div[@id='bgDiv']")
			bg_url = str(bg_div.value_of_css_property("background-image"))
			bg_url = bg_url[5:len(bg_url)-2]

			pic_dir = osutil.get_pic_directory()
			today = str(datetime.date.today())
			current_month = today[:-3]
			current_month_dir = pic_dir + os.path.sep + current_month
			osutil.check_and_make_directory(current_month_dir)

			img_name_from_url = re.sub("(.)*/", "", bg_url)
			fname = current_month_dir + "/" + today + "_" + img_name_from_url
	
			print "Retrieving image from Bing...."
			urllib.urlretrieve(bg_url, fname)
			print "\nImage downloaded and saved to path:" + current_month_dir + " under name:" + img_name_from_url

			get_info(today, driver)
			
			driver.quit()

			return fname
		else:
			print "Today's bing image of the day was set as wallpaper already."
	except:
		print "Unable to download image from Bing. Please try after sometime."
		raise

def get_info(today, driver):
	if click_element(driver, "//div[@class='hpcInfoText']"):
		try:
			info_div = driver.find_element_by_xpath("//div[@class='b_vPanel']")
			info = today + "\n" + info_div.text
			
			awesomeutil.set_today_and_info(info.encode("ascii", "ignore"))
		except:
			raise
			print try_later

def info():
	if not awesomeutil.today_set():
		driver = webdriver.Firefox()
		driver.get(bing)
		today = str(datetime.date.today())

		get_info(today, driver)

		driver.quit

	print awesomeutil.get_info()
