import pandas as pd
import numpy as np

# Array ################################################################################################################
# Array is nice for creating and managing matrix. Contrary to a list, all the element must be from the same type.
a = np.array([[1, 2, 3],
             [4, 5, 6]])

b = np.array([[4],
            [2],
            [1]])

# To multiply them
c = np.dot(a, b)

# To transpose a matrix
d = c.T


# Data managing ########################################################################################################

df = pd.read_excel('Data.xlsx')

df.set_index('Date', inplace=True)

returns = df.pct_change()

VL = (1+returns).cumprod()

VL.iloc[0, :] = 1

# Moving average
Moving_average = VL.rolling(window=10).mean().iloc[9:, :]


# Metrics ##############################################################################################################

# Correlation
import seaborn as sns
sns.heatmap(returns.corr())

# Matrix Variance Covariance
varcov = returns.cov()

def perf(VL: pd.DataFrame)-> float:
    return VL.iloc[-1, :]-1

# This volatility (=risk) is made for only one asset (Not for a portfolio). We multiply by 250 squared root cause we
# want to transform a volatility into an annual volatility
def vol(returns: pd.DataFrale)-> float:
    return returns.std()*250**0.5

# To make the results easier to read
tableau = pd.DataFrame({df.columns[1]:[VL.iloc[-1,1], returns.iloc[:, 1].std()*250**0.5],
                        df.columns[0]:[VL.iloc[-1,0]-1, returns.iloc[:, 0].std()*250**0.5]},
                       index=['Performance', 'Annualised Volatility'])

# Graph
import matplotlib.pyplot as plt

# This function calculates the volatility (=the risk) of a portfolio
# We have to minimize w'.varcov.w with w the matrix of weigths and varcov the variance covariance matrix based on returns
def vol(w, varcov):
    return np.sqrt(np.dot(w.T, np.dot(varcov,w)))


def min_vol(mean_returns, varcov, minmaxweigths):

    num_assets = len(mean_returns)
    args = (varcov)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x)-1})  # with 'ineq' inplace of 'eq' if you want an inequation

    return minimize(vol, # the first argument is the objective function
                    num_assets*[1./num_assets],  # it is an initial guess for the solver. It will start to optimize the
                    # objective function in trying this candidate
                    args = args,  # Arguments
                    method = 'SLSQP',  # Type of method
                    bounds = minmaxweigths,  # Constraints for each element of the solution
                    constraints = constraints,  # Constraints of the overall solution
                    tol = 1/np.power(10, 14))  # To impose a certain precision


minmaxweigths = [(0, 1), (0, 1)]

mean_returns = returns.mean()

import time

start = time.time()  # We save in start the exact time of the clock

weigths = min_vol(mean_returns, varcov, minmaxweigths)

print("--- %s seconds to find the solution with the solver ---" % (time.time() - start))

optweights = weights.x  # To have the values of the solution

message = weigths.message  # To have a message of the state of the solution

boolmessage = weights.success  # To have a boolean value to know if it found the optimum solution

solution = weigths.fun  # To have the value of the objective function with the optimum weigths


# Exercice to know if the solver seems to be nice ###############################################################

start = time.time()
better = False
result = []

for i in np.arange(0, 1, 0.00001):  # arange is like range but with a step (equal to the third argument)

    w = vol(np.array([i, 1-i]), varcov)
    result.append(w)

    if w <= solution:
        better = True
        break

print("--- %s seconds to find the solution with loop ---" % (time.time() - start))

if better:
    print("The solver has a problem")
else:
    print("the solver seems to be good because with iteration we douns a min vol portfolio equal to ", min(result),
          " and the min vol portfolio obtained by the solver is lover and equal to ", solution)

