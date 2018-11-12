from mainA import solution_a
from mainB import solution_b
import numpy as np
import pandas as pd
df = pd.DataFrame(columns = ['10^','solution 1 result','solution 2 result','solution 1 time','solution 2 time'])
upper_bound = 1000
for each in range(3):
    rd_num = np.random.random_integers(0,upper_bound,100)
    rea, sta, eta = solution_a(rd_num)
    reb, stb, etb = solution_b(rd_num)
    power = each + 3
    df.loc[each] = [power,rea,reb,(eta - sta),(etb - stb)]
    upper_bound *= 10
print(df)