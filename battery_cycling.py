import pandas as pd
file_name= AL_lithiated141_3form1ma_C08.txt
# Sample DataFrame with a series
data = pd.read_csv('file_name',' delimiter="\t", decimal=',')
df = pd.DataFrame(data)

# Initialize an empty list to store indices of sign changes
sign_change_indices = []

# Iterate over the series
for i in range(1, len(df)):
    # Check if the sign changes
    if (df['values'].iloc[i] >= 0 and df['values'].iloc[i-1] < 0) or (df['values'].iloc[i] < 0 and df['values'].iloc[i-1] >= 0):
        sign_change_indices.append(i)

print("What do you want to plot on the x- and y-axis?"
      "1:time(s),2:Potential(V),3:Capacity(mAh),4:Current(mA)")
x = input()
y= input()

print("Which cycle do you want to plot?")
cycle = input()
# print(sign_change_indices)
