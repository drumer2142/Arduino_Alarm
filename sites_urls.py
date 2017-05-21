import urllib.request


def scrap_page(url):
    web_data = urllib.request.urlopen(url)
    str_data = web_data.read()
    return str_data


def get_site_code(url):
    sites_code = urllib.request.urlopen(url).getcode()
    return sites_code
