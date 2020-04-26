import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('coeff.csv')
print('data: ', data)
x = data['Fuel(C)']
y1 = data['Data (Ea)']
# y2 = data['Simulation']
y3 = data['Simulation5']
y4 = data['Simulation10']

plt.plot(x,y1)
# plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)

plt.rc('text',usetex=True)
plt.title('Numerical and Analytical Result')
plt.xlabel('Fuel Length')
plt.ylabel('Ea')
plt.legend(loc='best')
plt.savefig('comparision.jpg')
plt.show()
