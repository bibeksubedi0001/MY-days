import pandas as pd  # Importing the pandas library
import numpy as np   # Importing numpy for handling numerical operations

# Step 1: Load the first CSV file into the DataFrame 'aa'
aa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Step 2: Introduce missing values (NaN) in the 'WindSpeed' column for the first two rows (index 0 and 1)
aa.loc[[0, 1], "WindSpeed"] = np.nan
print(aa)  # Print the DataFrame to see the changes

# Step 3: Print the information about the DataFrame
# This includes the number of non-null entries per column and the data types of each column
print(aa.info())

# Step 4: Check the number of missing values (NaN) in each column using isna().sum()
print(aa.isna().sum())

# Step 5: Fill missing values in 'WindSpeed' with the mean of the column
values = {"WindSpeed": aa["WindSpeed"].mean()}  # Calculate the mean of the 'WindSpeed' column
aa = aa.fillna(value=values)  # Replace missing 'WindSpeed' values with the mean value
print(aa)  # Print the DataFrame to inspect changes

# Step 6: Introduce missing values (NaN) in the 'WindSpeed' column for rows with index 4 and 6
aa.loc[[4, 6], "WindSpeed"] = np.nan
print(aa)  # Print the DataFrame to see the newly introduced missing values

# Step 7: Apply linear interpolation to the 'WindSpeed' column to fill in missing values
aa["WindSpeed"] = aa["WindSpeed"].interpolate()  # Linear interpolation to fill NaN values
print(aa)  # Print the DataFrame after interpolation to see the changes

# Step 8: Drop rows where 'Category' column has NaN values
print(aa.dropna(subset="Category"))  # Display the DataFrame after dropping rows with NaN in 'Category'

# Step 9: Filter rows where 'Category' column is NaN
print(aa[aa["Category"].isna()])  # Display rows where 'Category' is NaN

