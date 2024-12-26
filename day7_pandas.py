import pandas as pd

# Load the CSV file into a pandas DataFrame
qa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Display the total number of rows and columns
print(f"DataFrame loaded successfully with shape: {qa.shape}\n")

# Iterate over rows and display relevant details
for index, row in qa.iterrows():
    print(f"Index: {index}")  # Print the index of the row
    print("Row Data:")
    print(row.to_dict())  # Convert the Series (row) into a dictionary for cleaner output
    print("\n---\n")  # Separator for readability

    # Optional: Limit to first 10 rows for demonstration
    if index >= 9:
        print("Displayed first 10 rows only. Exiting loop...")
        break
