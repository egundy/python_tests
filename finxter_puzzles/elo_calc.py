'''This script is used to track elo progress in the puzzles from the book "Coffee Break Python".
   The script will find the current elo from a file "elo.pickle" and then ask the user if they got the question right or wrong.
   After the user answers, the script will modify the elo value in the .pickle file'''
import pickle
with open("elo.pickle" , "rb") as f:
    elo , puzzle = pickle.load(f)

#function to calculate the elo and return the new value
def elo_calc(elo , puzzle):
    print("This is your current elo: " + str(elo))
    print("This is your current puzzle:     " + str(puzzle))
    correct = input("Did you get the question correct? (y/n)     ")
    if correct == "y":
        if elo <= 499:
            elo += 46
        elif elo >= 500 and elo <= 999:
            elo += 33
        elif elo >=1000 and elo <=1499:
            elo += 11
        elif elo >= 1500 and elo <= 1999:
            elo += 8
        else: 
            elo += 8     
    elif correct == "n":
        if elo <= 499:
            elo -= 9
        elif elo >= 500 and elo <= 999:
            elo -= 22
        elif elo >=1000 and elo <=1499:
            elo -= 44
        elif elo >= 1500 and elo <= 1999:
            elo -= 47
        else: 
            elo -= 47   
    else:
        print("unknown entry please run the program again")
        exit()
    puzzle += 1
    with open("elo.pickle" , 'wb') as f:
        pickle.dump([elo , puzzle] , f)
    print("Your new elo is:     " + str(elo))
    print("Your new puzzle is:      " + str(puzzle))

elo_calc(elo,puzzle)