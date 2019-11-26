from datetime import datetime
import pytz
import sys
from tzlocal import get_localzone
from  timezones import countries

def display_time(time, zone = get_localzone()):
    year, month, month_str, day, hour, min, sec = map(str, time.strftime("%Y %m %B %d %H %M %S").split())
    print(str(zone) + "\n" + time.strftime("%H:%M:%S %d.%B (%d-%m-%Y)") + "\n")

def display_help():
    print("\n*countrycode* / *countryname* \n\tTo get current time in the country")
    print("\n-h / -help \n\tTo see help")
    print("\n-l / -list \n\tTo list available countries")

def list_countries():
    for country in countries:
        print("%s: %s" % (country['name'], country['code']))

def search_country(target):
    for country in countries:
        if target in country['name'].upper():
            display_country(country['code'])
    check_america(target)

def display_country(flag):
    flag = filter_flag(flag)
    for country in countries:
        if flag == country['code']:
            display_country_info(country)
            for timezone in country['timezones']:
                selected_timezone = pytz.timezone(timezone)
                display_time(datetime.now(selected_timezone), timezone)
            return True
    return False

def display_country_info(country):
    print(country['name'] + ': ' + country['code'])

def filter_flag(flag):
    if flag == 'UK': flag = 'GB'
    if flag == 'USA': flag = 'US'
    return flag

def check_america(flag):
    if flag in 'AMERICA':
        display_country('US')



def main():
    # Identify user input
    flag = None
    try:
        flag = sys.argv[1].upper()
    except:
        display_time(datetime.now())
        sys.exit()

    # Help command
    if flag == '-H' or flag == '-HELP':
        display_help()

    # List command
    if flag == '-L' or flag == '-LIST':
        list_countries()

    # Main functionality
    if display_country(flag) is False:
        search_country(flag)




# Entry
main()