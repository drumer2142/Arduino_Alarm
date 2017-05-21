import bs4
import sites_urls


def make_soup(source, main_dict):
    soup = bs4.BeautifulSoup(source, 'lxml')

    # find all the H2 tags
    header_two_arr = soup.find_all('h2')

    # find all the ul elements and append them into an array
    # for further processing
    unordered_list_arr = soup.find_all('ul')

    # Soup2 outputs all the strikes for today
    soup2 = bs4.BeautifulSoup(str(unordered_list_arr[0]), "lxml")
    sorted_list1 = soup2.find_all('li')
    todays_strikes = []
    # iterate thought vars and insert them to arrays
    for j in range(len(sorted_list1)):
        # print("Today: ", str(sorted_list1[j].text))
        # append strikes to an array for more processing
        # append it because it is object
        todays_strikes.append(str(sorted_list1[j].text))


    # Soup3 outputs all the strikes for tomorrow
    soup3 = bs4.BeautifulSoup(str(unordered_list_arr[1]), "lxml")
    sorted_list2 = soup3.find_all('li')
    tomorrows_strikes = []
    # iterate thought vars and insert them to arrays
    for i in range(len(sorted_list2)):
        # print("Tomorrow: ", str(sorted_list2[i].text))
        # append strikes to an array for more processing
        tomorrows_strikes.append(str(sorted_list2[i].text))

    main_dict["todays_strikes"] = todays_strikes
    main_dict["tomorrows_strikes"] = tomorrows_strikes


def strikes_url(url, main_dict):
    # check if status code is 200 else output an error
    # if the website is down
    if sites_urls.get_site_code(url) == 200:
        source = sites_urls.scrap_page(url)
        make_soup(source, main_dict)
    else:
        print("It appears that the site apergia.gr is not reachable at the moment")
