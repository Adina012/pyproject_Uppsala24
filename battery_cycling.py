import pandas as pd
import matplotlib.pyplot as plt
'''
This code helps you to plot the experimental data from lithiation/delithiation of a Li half-cell. First it loads a txt-file 
with the data and converts it to a data-frame.It will then create a list of the indices of the points were the sign of the 
current changes. This list will make it possible to choose which lithiation/delithiation you want to plot.
Then you are asked what you want to plot on the respective axis:
1:time(s),2:Potential(V),3:Capacity(mAh),4:Current(mA). 
'''

# The txt-file contains 5 columns with experimental data in scientific notation,
# tab-delimited and ',' as decimal separator. The experimental data comes from a potentiostat and consists of cycle no.,
# time(s),potential(V),capacity(mAh) and current(mA).
data = pd.read_csv('AL_lithiated141_3form1ma_C08.txt', delimiter="\t", decimal=",")
df = pd.DataFrame(data)

# Initialize an empty list to store indices of sign changes
sign_change_indices = [],

# Iterate over the series
for i in range(4, len(df)):
    # Check if the sign changes
    if (df['values'].iloc[i] >= 0 and df['values'].iloc[i-1] < 0) or (df['values'].iloc[i] < 0 and df['values'].iloc[i-1] >= 0):
        sign_change_indices.append(i)

print("What do you want to plot on the x- and y-axis?"
      "1:time(s),2:Potential(V),3:Capacity(mAh),4:Current(mA)")
x = input()
y= input()

print("Which lithiation/delithiation do you want to plot?"
      "Example: If you want to plot the 1st lithiation give input 1, and for 1st delithiation typ 2,"
      "so to plot the 10th lithiation type 20, and the 10th delithiation type 21.")
no_de_lithiation = input()


if x==1 and y==2:
    plt.plot()


#plt.plot(df.iloc[:, _], df.iloc[:, _])