import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('AL_lithiated141_3form1ma_C08.txt', delimiter="\t", decimal=",")
df = pd.DataFrame(data)

# Initialize an empty list to store indices of sign changes
sign_change_indices = []

# Iterate over the series
for i in range(len(df) - 1):
    # Check if the sign changes
    if (df.iloc[i, 4] >= 0 and df.iloc[i + 1, 4] < 0) or (df.iloc[i, 4] < 0 and df.iloc[i + 1, 4] >= 0):
        sign_change_indices.append(i)

#Choose which series you want to plot
print("What do you want to plot on the x- and y-axis?"
      "1:time(s),2:Potential(V),3:Capacity(mAh),4:Current(mA)")
x = int(input())
y = int(input())
#Choose which part of the data you want to plot, ie the 1st,2nd,3d...lithiation or delithiation.
print("Which lithiation/delithiation do you want to plot?"
      "Example: If you want to plot the 1st lithiation give input 1, and for 1st delithiation type 2,"
      "so to plot the 10th lithiation type 10, and the 10th delithiation type 20.")
no_de_lithiation = int(input())

# Check if the input is valid
if no_de_lithiation <= 0 or no_de_lithiation > len(sign_change_indices):
    print("Invalid lithiation/delithiation number.")
else:
    # Extract the start and end indices for the chosen lithiation/delithiation
    start_index = sign_change_indices[no_de_lithiation-1]
    end_index = sign_change_indices[no_de_lithiation]
    # If the chosen series to plot on the x-axis is time, it is converted to hours.
    if x ==1:
        plt.plot(df.iloc[start_index:end_index, x/3600], df.iloc[start_index:end_index, y])
        plt.xlabel('Time(h)')
        # If the chosen series to plot on the x-axis is capacity, the code asks for the active mass(in grams) of the electrode
        # and normalizes the data with this mass.
    elif x==3:
        print('What is the active mass(g) of the electrode?')
        m=float(input())

        plt.plot(df.iloc[start_index:end_index, x]/m, df.iloc[start_index:end_index, y])
        plt.xlabel('Capacity(mAh/g)')

    else:
        plt.plot(df.iloc[start_index:end_index,x], df.iloc[start_index:end_index,y])
        plt.xlabel(df.columns[x])
# The final diagram of the chosen experimental data i plotted.
    plt.ylabel(df.columns[y])
    plt.title(f"Lithiation/Delithiation {no_de_lithiation}")
    plt.show()
