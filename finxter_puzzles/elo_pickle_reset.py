#resets pickle file variables to zero
import pickle
elo = 0
puzzle = 0
with open("elo.pickle" , "wb") as f:
    pickle.dump([elo , puzzle] , f)
