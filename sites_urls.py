import urllib.request

def scrap_page(url):
	
	try:
		web_data = urllib.request.urlopen(url)
		str_data = web_data.read()
		return str_data
  
	except:
		print("Something went wrong trying tp request the url open")


def get_site_code(url):
    sites_code = urllib.request.urlopen(url).getcode()
    return sites_code
