from py_files import name_days
from py_files import strikes
from py_files import date_and_time_is as dt_is
from pymongo import MongoClient as mgc
import cfg as setup


def insert_mongo(main_dict):
    client = mgc(setup.server['IP'], 27017)
    db = client.Arduino_Alarm
    collection = db.alarm_data
    post_main = {"name_of_day": main_dict["name_of_day"], "month": main_dict["month"], "day_no": main_dict["day_no"], "time": main_dict["time"], "year": main_dict["year"], "todays_strikes": main_dict["todays_strikes"], "tomorrows_strikes": main_dict["tomorrows_strikes"], "todays_name_days": main_dict["todays_name_days"], "tomorrows_name_days": main_dict["tomorrows_name_days"]}
    post_db = collection.insert_one(post_main)



def main():
    # main dictionary for appending and retracting data
    main_dict = {}

    # create object of date time module
    # variables to access: day month day_no time year
    date_time_is = dt_is.runDT_is()
    # print("New Tuple data: ", date_time_is)
    # get the original name of day
    original_nod = dt_is.get_name_of_day(date_time_is.day)
    # print("Today the day is --> ", original_nod)

    main_dict["name_of_day"] = original_nod
    main_dict["month"] = date_time_is.month[0]
    main_dict["day_no"] = date_time_is.day_no[0]
    main_dict["time"] = date_time_is.time[0]
    main_dict["year"] = date_time_is.year[0]
    

    if setup.server['UseScrappers'] == 'True':
        
        #original url
        url = setup.urls['strikes']
        scrape_strikes = strikes.strikes_url(url, main_dict)

    
        #name days original url
        name_days_url = setup.urls['namedays']
        scrape_namedays = name_days.find_name_days(name_days_url, main_dict)

    if setup.server['UseMongo'] == 'True' and (scrape_strikes != False and scrape_namedays != False):
        # insert data to mongoDB
        insert_mongo(main_dict)
    
    # if (scrape_strikes != False and scrape_namedays != False):
    #     print(main_dict["name_of_day"])
    #     print(main_dict["month"])
    #     print(main_dict["day_no"])
    #     print(main_dict["time"])
    #     print(main_dict["year"])
    #     print(main_dict["todays_strikes"])
    #     print(main_dict["tomorrows_strikes"])
    #     print(main_dict["todays_name_days"])
    #     print(main_dict["tomorrows_name_days"])


if __name__ == '__main__':
    main()
