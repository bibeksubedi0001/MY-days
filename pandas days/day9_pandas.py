import pandas as pd
import numpy as np

# Load the CSV file
aa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Step 1: Add a new column "Location" with all values set to "Nepal"
aa["Location"] = "Nepal"

# Step 2: Add a new column "Old_Location" with conditional values
aa["Old_Location"] = np.where(aa["name"] == "Bibek", "Myagdi", "Zombie")

# Step 3: Drop the row with index 0
aa = aa.drop(0)

# Step 4: Drop the "Location" column
aa.drop(columns=["Location"], inplace=True)

# Step 5: Reorder columns for better readability
aa = aa[["name", "Humidity", "Old_Location", "WindSpeed", "Date", "Category"]]

# Step 6: Add a new column "NEW_PARA" by multiplying "Humidity" and "WindSpeed"
aa["NEW_PARA"] = aa["Humidity"] * aa["WindSpeed"]

# Step 7: Rename the "WindSpeed" column to "Old_PARA"
aa = aa.rename(columns={"WindSpeed": "Old_PARA"})

# Display the final DataFrame
print("\nFinal DataFrame:")
print(aa.head())

# Save the final DataFrame to a new CSV file
output_path = r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\updated_rainfall_data_final.csv"
aa.to_csv(output_path, index=False)
print(f"\nFinal DataFrame saved to: {output_path}")
