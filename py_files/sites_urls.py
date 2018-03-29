import urllib.request

def scrap_page(url):
	
	try:
		web_data = urllib.request.urlopen(url)
		str_data = web_data.read()
		return str_data
  
	except Exception as e:
		print("Something went wrong trying to query the url")
		print("Error: ", str(e))
		return False


def get_site_code(url):
    sites_code = urllib.request.urlopen(url).getcode()
    return sites_code
