import pandas as pd  # Import pandas for data manipulation

# Step 1: Load the CSV file into a pandas DataFrame
# Ensure the file path is correct and accessible
try:
    qa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")
    print("CSV file loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    qa = None

# Proceed only if the file is successfully loaded
if qa is not None:
    # Step 2: Display the first few rows to understand the structure of the DataFrame
    print("\nFirst 5 rows of the DataFrame:")
    print(qa.head())
    
    # Step 3: Check for missing data in the DataFrame
    print("\nMissing values in each column:")
    print(qa.isnull().sum())  # Count of missing values per column

    # Fill missing values in the "Precipitation" column (if any) with 0
    if "Precipitation" in qa.columns:
        qa["Precipitation"].fillna(0, inplace=True)
        print("\nMissing values in 'Precipitation' filled with 0.")

    # Step 4: Access specific data points using `at` and `iat`
    # Access the value at row index 0 and column "Precipitation" using `at`
    print("\nValue at row 0, column 'Precipitation':")
    print(qa.at[0, "Precipitation"] if "Precipitation" in qa.columns else "Column 'Precipitation' not found.")

    # Access the value at row index 0 and column index 0 using `iat`
    print("\nValue at row 0, column 0:")
    print(qa.iat[0, 0])

    # Step 5: Accessing a column in two different ways
    # Using dot notation
    print("\nAccessing 'Date' column using dot notation (qa.Date):")
    try:
        print(qa.Date)
    except AttributeError:
        print("Error: Column 'Date' cannot be accessed with dot notation. Use bracket notation instead.")

    # Using bracket notation
    print("\nAccessing 'Date' column using bracket notation (qa['Date']):")
    if "Date" in qa.columns:
        print(qa["Date"])
    else:
        print("Column 'Date' not found in the DataFrame.")

    # Step 6: Sorting the DataFrame by the "Precipitation" column
    if "Precipitation" in qa.columns:
        # Sort in ascending order
        print("\nDataFrame sorted by 'Precipitation' in ascending order:")
        print(qa.sort_values("Precipitation").head())  # Display top 5 rows of the sorted DataFrame

        # Sort in descending order
        print("\nDataFrame sorted by 'Precipitation' in descending order:")
        print(qa.sort_values("Precipitation", ascending=False).head())  # Display top 5 rows of the sorted DataFrame

        # Save the sorted DataFrame to a new CSV file
        try:
            qa_sorted = qa.sort_values("Precipitation", ascending=False)
            qa_sorted.to_csv(r"D:\for_my_portfolio\sorted_rainfall_data.csv", index=False)
            print("\nSorted DataFrame saved to 'sorted_rainfall_data.csv'.")
        except Exception as e:
            print(f"Error: Failed to save the sorted DataFrame. {e}")

    # Step 7: Filtering Data
    # Display rows with "Precipitation" greater than 0.5
    if "Precipitation" in qa.columns:
        print("\nRows with 'Precipitation' > 0.5:")
        high_precipitation = qa[qa["Precipitation"] > 0.5]
        print(high_precipitation.head())  # Display first 5 rows of filtered data

    # Step 8: Descriptive Statistics
    print("\nDescriptive statistics of the numerical columns:")
    print(qa.describe())

    # Step 9: Check for duplicate rows
    print("\nNumber of duplicate rows in the DataFrame:")
    print(qa.duplicated().sum())

    # Optionally, drop duplicate rows
    print("\nDropping duplicate rows (if any).")
    qa.drop_duplicates(inplace=True)
    print(f"Shape of DataFrame after dropping duplicates: {qa.shape}")
