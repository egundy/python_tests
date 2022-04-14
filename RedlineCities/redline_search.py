''' This script is intended to search through data on redlining within the
    United States of America, and return relevant data based on search query'''

# imports
import pandas as pd

# dataframe
df = pd.read_csv('redlining.csv')

# search functions
# state search
def state_search():
    print("\nYou chose: state search")
    state = input("What state do you want to search for? (Abbreviation only) press 'enter' to exit\n")
    if state == ():
        exit
    else:
        print(df[df["state"] == state])
# city search
def city_search():
    print("\nYou chose: city search")
    city = input("What city do you want to search for? press 'enter' to exit\n")
    if city == ():
        exit
    else:
        print(df[df["city"] == city])
# year search
def year_search():
    print("\nYou chose: year search")
    year = input("What year do you want to search for? press 'enter' to exit\n")
    if year == ():
        exit
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
type = input("What category do you want to search for?\n(Options: state, city, year) press 'enter' to exit\n\n")
if type == ():
    exit
search_type(type)