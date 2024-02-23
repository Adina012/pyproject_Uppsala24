import matplotlib.pyplot as plt
import pandas as pd
# exp_data is a dataframe containing experimental data. It has series "vectors" with titles
# in the first "series". 0: cycle number, 1: time(s), 2: Potential (V), 3: Capacity (mAh), 4: Current (mA)
exp_data = pd.read_csv('19kura200ul128cc-01cv_C09.txt', delimiter="\t", decimal=',')


mass = 8.55E-3  # active mass HC of electrode in g
plt.plot(exp_data.iloc[:, 3]/mass, exp_data.iloc[:, 2])

plt.xlabel("Capacity mAh/g")
plt.ylabel("Voltage(V)")
# plt.legend(['Cell 1.2'],['Cell 1.4'])
plt.show()