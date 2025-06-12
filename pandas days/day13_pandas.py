import pandas as pd  # Importing the pandas library
import numpy as np   # Importing numpy for handling numerical operations

# Step 1: Load the first CSV file into the DataFrame 'aa'
aa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Checking the value counts of the 'Category' column
print(aa["Category"].value_counts())

# Filtering the rows where Precipitation is less than 25 and checking the 'Category' value counts
print(aa[aa["Precipitation"] < 25]["Category"].value_counts())

# Calculating the mean of Precipitation where WindSpeed is greater than 2.5
print(aa[aa["WindSpeed"] > 2.5]["Precipitation"].mean())

# Interpolating missing values in the DataFrame
aa = aa.interpolate()

# Displaying the DataFrame after interpolation
print(aa)

# Grouping by 'Category' and calculating the mean of 'Precipitation' for each group
print(aa.groupby(["Category"])["Precipitation"].mean())

# Performing multiple aggregations (sum of 'Precipitation' and mean of 'WindSpeed') for each 'Category'
print(aa.groupby(["Category"]).agg({"Precipitation": "sum", "WindSpeed": "mean"}))

# Creating a pivot table where 'Category' is the columns, 'Date' is the index, and 'Humidity' is the values
pivot = aa.pivot(columns="Category", index="Date", values="Humidity")

# Displaying the pivot table
print(pivot)

# Interpolating missing values in the pivot table
pivot = pivot.interpolate()

# Displaying the pivot table after interpolation
print(pivot)

# Accessing a specific value from the pivot table (Humidity for "Heavy" category on "1/1/2019 5:00")
print(pivot.loc["1/1/2019 5:00", "Heavy"])

# Summing across columns (i.e., summing the values for each row)
print(pivot.sum(axis=1))
