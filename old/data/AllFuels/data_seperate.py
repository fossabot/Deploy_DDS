import pandas as pd
import numpy as np

dataset = pd.read_csv('Alkane_Dataset.csv')

uniq_fuel = dataset['Fuel'].unique()

for i in range(len(uniq_fuel)):
	data_seperated = dataset[dataset['Fuel'] == uniq_fuel[i]]
	data_seperated.to_csv(str(uniq_fuel[i])+'.csv',index = None)
	data_seperated[0:0]

