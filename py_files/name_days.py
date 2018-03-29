from py_files import sites_urls
import xml.etree.ElementTree as et
from py_files import logging as log


def form_xml(str_data):
    return et.fromstring(str_data)


def find_name_days(name_days_url, main_dict):
    try:

        scrapped_data = sites_urls.scrap_page(name_days_url)

    except Exception as ex:
        error_msg = "It appears that the site eortologio.gr is not reachable at the moment"
		log.log_error("name_days", error_msg)

        print(error_msg)
        print("Error: ", str(e))
        return False

    xml_data = form_xml(scrapped_data)
    channel = xml_data.findall("channel")

    # init empty arrays for namedays
    todays_namedays = []
    tommorows_namedays = []

    for x in channel:
        item = x.findall("item")
        tmp_count = 0
        for y in item:
            name_days_title = y.find("title").text
            name_days_title_split = name_days_title.split()
            # Split in to different array for easier processing
            # Not using append because it creates second dimension
            if tmp_count == 0:
                todays_namedays = todays_namedays + name_days_title_split
            elif tmp_count == 1:
                tommorows_namedays = tommorows_namedays + name_days_title_split

            # add to count 1
            tmp_count = tmp_count + 1
    process_nameday_arrays(todays_namedays, tommorows_namedays, main_dict)

    # parse to process_nameday_arrays for more splitting
    #process_nameday_arrays(todays_namedays, tommorows_namedays, main_dict)


def process_nameday_arrays(todays_namedays, tommorows_namedays, main_dict):
    # debug arrays
    # print(todays_namedays)
    # print(tommorows_namedays)

    # after the sixth position of the array the names start it is fixed

    todays_only_names = todays_namedays[6:-3]
    # print("Today: ", todays_only_names)

    tommorows_only_names = tommorows_namedays[6:-3]
    # print("Tomorrow: ", tommorows_only_names)

    main_dict["todays_name_days"] = todays_only_names
    main_dict["tomorrows_name_days"] = tommorows_only_names

