import numpy as np
import pandas as pd

titanic = pd.read_csv("titanic_data.csv")
ages = titanic["Age"]
fare = titanic["Fare"]
surv = titanic["Survived"]

print(surv.describe)
