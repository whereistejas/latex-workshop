import matplotlib.pyplot as plt
import random as rd

years = rd.sample(range(2000, 2010), 10)
amount=  rd.sample(range(100,200), 10)
amount1= rd.sample(range(100,200), 10)

plt.plot(years, amount)
plt.savefig("plot1.pdf")
plt.savefig("plot1.png")
plt.plot(years, amount1)
plt.savefig("plot2.pdf")
