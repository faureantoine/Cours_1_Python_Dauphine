import pandas as pd

# This is our DataFrame, with the returns per day for rows and assets in columns
df = pd.DataFrame([[-0.03, 0.01, 0.01], [0.02, -0.02, -0.01], [-0.01, -0.04, -0.01], [-0.02, 0.01, -0.02]],
                  columns=['asset 1', 'asset 2', 'asset 3'])

day = ['Day 1', 'Day 3']

''' Add 'Day 2' to the second position of the list day :'''
day.insert(1, 'Day 2')

'''Add 'Day 4' to the last position of the list day :'''
day.append('Day 4')

'''Put the list day in index of the DataFrame df :'''
df.index = day

'''
We would like to calculate how many returns was negatives in our portfolio
'''

'''The first method is to use two loops and to check for each return if it is negative or not'''
nb = 0

for i in range(len(df. columns)):  # First loop for the columns
    for j in range(len(df.index)):  # Second loop for the rows
        if df.iloc[j, i] <= 0:
            nb += 1  # increment nb by +1


'''
Second way is to use boolean and to count how many boolean are True
'''

dfNew = (df <= 0)
nb2 = sum(sum(dfNew.values))

''' Check if the two results found before are the same '''
if nb2 == nb:
    print("It seems to be good")
else:
    print("there is a problem")