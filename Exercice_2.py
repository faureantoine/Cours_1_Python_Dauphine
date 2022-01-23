'''
Black and Scholes model prices European Options.
An option is the right to buy or sell an underlying asset (it can be a stocks for instance)
A Call is an option to buy something
A Put is an option to sell something
For any option, you need someone who buy it (long) and someone who sell it (short)
A long Call is the right to buy the underlying asset for a fixed priced (the price fixed in advanced is called strike)
at a date fixed in advanced (for european option).
A short Call is the fact to sell the call option.
The person who bought the Call will exercice the option if at the maturity date the price of the underlying
asset is superior to the strike. For instance if the price of a stock (that is the underlying asset) is equal to 100 and
that the strike is 80, the person who is long call will exercice the option cause he can buy the stock for 80 whereas the
value of the stock in the market is 100. His payoff is equal to 20. Whereas the person who is short call will have a
payoff of -20.
American option can be exerciced during all the life of the option. So at any time until the maturity date.
'''

# Fill the blanks

class Bs:
    def __init__(self, typ, r, vol, t, mu, k, s0):
        self.typ=typ
        self.r = r
        self.vol = vol
        self.T = t
        self.mu = mu
        self.k = k
        self.S0 = s0
        self. ...  # we call the method pricing


    def pricing(...):
        self.price = self.typ * (
                    self.S0 * norm.cdf(self.typ * ...) - self.k * math.exp(-... * ...) * norm.cdf(
                self.typ * self. ... ))

    def d1(...):
        return (np.log(... / ...) + (self.r + self.vol ** ... / 2) * self.T) / (self.vol * (...)**...)

    def d2(...):
        return ... - self.vol * (self.T)**...


r = 0.01  # Risk free
vol = 0.1  # Volatility (risk)
T = 10  # Time to maturity, in years
mu = 0.1  # Mean return
k = 100  # strike
S0 = 100  # Current price of the underlying asset


# Creat an object of the class Bs with the inputs given and for a Call
Mypricer1 = Bs(1, r, vol, T, mu, k, S0)

CallPrice = Mypricer1.price  # Save the call price

# Creat an object of the class Bs with the inputs given and for a Call
Mypricer2 = Bs(-1, r, vol, T, mu, k, S0)

PutPrice = Mypricer2. ...  # Save the put price

