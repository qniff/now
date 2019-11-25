from datetime import datetime
import pytz
import sys
from tzlocal import get_localzone
from  timezones import countries


def display_time(time, zone = get_localzone()):
    year, month, month_str, day, hour, min, sec = map(str, time.strftime("%Y %m %B %d %H %M %S").split())
    to_print = time.strftime("%H:%M:%S %d.%B (%d-%m-%Y)")
    print(zone, "\n", to_print, "\n")

def display_help():
    print("\n*countrycode* / *countryname* \n\tTo get current time in the country")
    print("-h / -help \n\tTo see help")
    print("-l / -list \n\tTo list available countries")

def list_countries():
    for country in countries:
        to_print = ("%s: %s" % (country['name'], country['code']))
        print(to_print)

def search_country(target):
    for country in countries:
        if target in country['name'].upper():
            display_country(country['code'])

def display_country(flag):
    for country in countries:
        if flag == country['code']:
            display_country_info(country)
            for timezone in country['timezones']:
                selected_timezone = pytz.timezone(timezone)
                display_time(datetime.now(selected_timezone), timezone)
            return True
    return False

def display_country_info(country):
    print(country['name'] + ': ' + country['code'] + '\n')



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