''' This script is intended to search through data on redlining within the
    United States of America, and return relevant data based on search query'''

# imports
import pandas as pd

# color class
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# dataframe
df = pd.read_csv('redlinedCities.csv')

# search functions
# state search
def state_search():
    n = 0
    while n == 0:
        print(color.BLUE + "\nYou chose: state search" + color.END)
        state = input(color.BLUE + "What state do you want to search for? (Abbreviation only) type 'back' to return to category selector\n" + color.END)
        if state == ('back'):
            n = 1
        else:
            print(df[df["state"] == state])
# city search
def city_search():
    n = 0
    while n == 0:
        print(color.YELLOW + "\nYou chose: city search" + color.END)
        city = input(color.YELLOW + "What city do you want to search for? type 'back' to return to category selector\n" + color.END)
        if city == ('back'):
            n = 1
        else:
            print(df[df["city"] == city])
# year search
def year_search():
    n = 0
    while n == 0:
        print(color.GREEN + "\nYou chose: year search" + color.END)
        year = input(color.GREEN + "What year do you want to search for? type 'back' to return to category selector\n" + color.END)
        if year == ('back'):
            n = 1
        else:
            print(df[df["year"] == year])

# search type
def search_type(type):
    match type:
        case "state":
            state_search()
        case "State":
            state_search()
        case "City":
            city_search()
        case "city":
            city_search()
        case "year":
            year_search()
        case "Year":
            year_search()
        case _: 
            return color.BLUE + "Unable to search for that category" + color.END
  
# main
n = 0
while n == 0:
    type = input(color.DARKCYAN + "What category do you want to search for?\n(Options: state, city, year) type 'exit' to exit\n\n" + color.END)
    if type == ('exit'):
        n = 1
    search_type(type)