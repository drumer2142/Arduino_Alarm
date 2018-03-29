import urllib.request
from py_files import logging as log

def scrap_page(url):
	
	try:
		web_data = urllib.request.urlopen(url)
		str_data = web_data.read()
		return str_data
  
	except Exception as e:
		error_msg = "Something went wrong trying to query the url"
		log.log_error("urllib_requests", error_msg)

		print(error_msg)
		print("Error: ", str(e))
		return False


def get_site_code(url):
    sites_code = urllib.request.urlopen(url).getcode()
    return sites_code
