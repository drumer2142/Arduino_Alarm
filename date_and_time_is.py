from time import ctime
from collections import namedtuple


def getDT_Data():
    current_data = ctime()
    return current_data


def runDT_is():
    data_are = getDT_Data()
    # print(data_are)
    data_are_split = data_are.split(" ")
    # print("Data Split Array: ", data_are_split)

    if data_are_split[3] == " ":
        # create a namedtuple to use as an object in index file
        date_time_tuple_space = namedtuple('Date_Time', 'day month space day_no time year')
        # create the tuple data
        date_time_is = date_time_tuple_space(data_are_split[0:1], data_are_split[1:2], data_are_split[2:3], data_are_split[3:4], data_are_split[4:5], data_are_split[5:6])
    else:
        # create a namedtuple without the possible space generated by the digits
        date_time_tuple_NoSpace = namedtuple('Date_Time', 'day month day_no time year')
        # create the tuple data without the space
        date_time_is = date_time_tuple_NoSpace(data_are_split[0:1], data_are_split[1:2], data_are_split[2:3], data_are_split[3:4], data_are_split[4:5])
    # print("Tuple Array: ", date_time_is)
    return date_time_is


def get_name_of_day(day_name):
    name_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # declare vars
    i = 0
    # nod = name of day
    nod = ""
    while i < len(name_days_list):
        nod = name_days_list[i]
        if str(day_name[0]) == nod[:3]:
            break
        i += 1
    # return original name of day
    return nod
