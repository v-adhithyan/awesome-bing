from distutils.core import setup

setup(
	name = "awesome_bing",
	packages = ["awesome_bing"],
	version = '0.1',
	description = "A python utility to view today's bing wallpaper, its information and set as wallpaper",
	author = "Adhithyan V",
	author_email = "aavispeaks@gmail.com",
	url = "https://github.com/v-adhithyan/awesome-bing",
	download_url = "https://github.com/v-adhithyan/awesome-bing/tarball/0.1",
	keywords = [ 'bing', 'wallpaper', 'download'],
	install_requires=['selenium'],
	classifiers = [],
	scripts=['bin/awesome-bing'],
)
