import pandas as pd

df = pd.read_csv("/home/mio/Documents/code/GDSC/GDSC2-dataset.csv")
# Separate rows with null values
df_with_nulls = df[df.isnull().any(axis=1)]

# Separate rows without null values
df_without_nulls = df[~df.isnull().any(axis=1)]

# Save each DataFrame to a CSV file
df_with_nulls.to_csv('GDSC2_with_nulls.csv', index=False)
df_without_nulls.to_csv('GDSC2_without_nulls.csv', index=False)

print("Data saved successfully to 'data_with_nulls.csv' and 'data_without_nulls.csv'.")
