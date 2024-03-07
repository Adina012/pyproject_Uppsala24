import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('AL_lithiated141_3form1ma_C08.txt', delimiter="\t", decimal=",")
df = pd.DataFrame(data)

# Initialize an empty list to store indices of sign changes
sign_change_indices = []

# Iterate over the series
for i in range(1, len(df)):
    # Check if the sign changes
    if (df['Current(mA)'].iloc[i] >= 0 and df['Current(mA)'].iloc[i-1] < 0) or (df['Current(mA)'].iloc[i] < 0 and df['Current(mA)'].iloc[i-1] >= 0):
        sign_change_indices.append(i)

print("What do you want to plot on the x- and y-axis?"
      "1:time(s),2:Potential(V),3:Capacity(mAh),4:Current(mA)")
x = int(input())
y = int(input())

print("Which lithiation/delithiation do you want to plot?"
      "Example: If you want to plot the 1st lithiation give input 1, and for 1st delithiation type 2,"
      "so to plot the 10th lithiation type 10, and the 10th delithiation type 20.")
no_de_lithiation = int(input())

# Check if the input is valid
if no_de_lithiation <= 0 or no_de_lithiation > len(sign_change_indices):
    print("Invalid lithiation/delithiation number.")
else:
    # Extract the start and end indices for the chosen lithiation/delithiation
    start_index = sign_change_indices[no_de_lithiation - 1]
    if no_de_lithiation == len(sign_change_indices):
        end_index = len(df)
    else:
        end_index = sign_change_indices[no_de_lithiation]

    # Plot the selected data
    plt.plot(df.iloc[start_index:end_index, x], df.iloc[start_index:end_index, y])
    plt.xlabel(df.columns[x])
    plt.ylabel(df.columns[y])
    plt.title(f"Lithiation/Delithiation {no_de_lithiation}")
    plt.show()


#plt.plot(df.iloc[:, _], df.iloc[:, _])