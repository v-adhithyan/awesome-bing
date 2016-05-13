import os
import re
from selenium import webdriver
import time
import urllib
import datetime

bing = "http://www.bing.com"
driver = webdriver.Firefox()
driver.get(bing)

bg_div = driver.find_element_by_xpath("//div[@id='bgDiv']")
bg_url = str(bg_div.value_of_css_property("background-image"))
bg_url = bg_url[5:len(bg_url)-2]

pic_dir = "/Users/adhithyan-3592/Pictures/bing/"
today = str(datetime.date.today())
current_month = today[:-3]
current_month_dir = pic_dir + current_month
if not os.path.exists(current_month_dir):
	os.makedirs(current_month_dir)

img_name_from_url = re.sub("(.)*/", "", bg_url)
fname = current_month_dir + "/" + today + "_" + img_name_from_url
urllib.urlretrieve(bg_url, fname)

os.system('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "' + fname + '"\'')

driver.quit()
