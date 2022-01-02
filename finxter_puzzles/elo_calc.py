'''This should work to create a script which will calculate my elo for puzzles with finxter and then output them to a file.'''

current_puzzle = 1
print("You are currently on puzzle " + str(current_puzzle) + ".")
#elo = input("Did you get the puzzle correct? Y/N") #flag...this is not the right code come back later

#function to calculate the elo and return the new value
def elo_calc(elo):
    print("This is your current elo: " + str(elo))
    correct = input("Did you get the question correct? (y/n)     ")
    print(correct)
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
    print("Your new elo is:     " + str(elo))
        

elo_calc(1500)
