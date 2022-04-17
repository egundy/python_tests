''' This script is intended to search through data on redlining within the
    United States of America, and return relevant data based on search query'''

# imports
import pandas as pd

# dataframe
df = pd.read_csv('redlinedCities.csv')

# search functions
# state search
def state_search():
    n = 0
    while n == 0:
        print("\nYou chose: state search")
        state = input("What state do you want to search for? (Abbreviation only) type 'back' to return to category selector\n")
        if state == ('exit'):
            n = 1
        else:
            print(df[df["state"] == state])
# city search
def city_search():
    n = 0
    while n == 0:
        print("\nYou chose: city search")
        city = input("What city do you want to search for? type 'back' to return to category selector\n")
        if city == ('back'):
            n = 1
        else:
            print(df[df["city"] == city])
# year search
def year_search():
    n = 0
    while n == 0:
        print("\nYou chose: year search")
        year = input("What year do you want to search for? type 'back' to return to category selector\n")
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
            return "Unable to search for that category"
  
# main
n = 0
while n == 0:
    type = input("What category do you want to search for?\n(Options: state, city, year) type 'exit' to exit\n\n")
    if type == ('exit'):
        n = 1
    search_type(type)