'''This script is used to track elo progress in the puzzles from the book "Coffee Break Python".
   The script will find the current elo from a file "elo.txt" and then ask the user if they got the question right or wrong.
   After the user answers, the script will modify the elo value in the .txt file'''
   
   
   
# The .txt file has yet to be integrated and as such the elo will be set to whatever the user wants.
# Also, the current puzzle will always be set to one until the .txt file is set up.
current_puzzle = 1
print("You are currently on puzzle " + str(current_puzzle) + ".")

#functions

#function to calculate the elo and return the new value
def elo_calc(elo):
    print("This is your current elo: " + str(elo))
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
    print("Your new elo is:     " + str(elo))
        
x = int(input("What elo do you have?     "))
elo_calc(x)
