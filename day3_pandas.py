import pandas as pd  # Importing the pandas library

# Step 1: Load the CSV file into a pandas DataFrame
try:
    afall = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")
    print("CSV file loaded successfully!")
except FileNotFoundError:
    print("Error: The specified CSV file could not be found. Please check the file path.")
    afall = None
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
    afall = None

if afall is not None:
    # Display the first 5 rows of the rainfall data
    print("\nFirst 5 rows of the Rainfall Time Series DataFrame:")
    print(afall.head())
    
    # Display column names
    print("\nColumn names in the Rainfall DataFrame:")
    print(afall.columns.tolist())
    
    # Display the total number of rows and columns
    print("\nShape of the Rainfall DataFrame (rows, columns):")
    print(afall.shape)

    # Check for missing data
    print("\nNumber of missing values in each column of the Rainfall DataFrame:")
    print(afall.isnull().sum())

# Step 2: Load the Excel file into a pandas DataFrame
try:
    adal = pd.read_excel(r"C:\Users\Bibek\Documents\project\data\Wind Speed for Stations.xlsx")
    print("\nExcel file loaded successfully!")
except FileNotFoundError:
    print("Error: The specified Excel file could not be found. Please check the file path.")
    adal = None
except pd.errors.EmptyDataError:
    print("Error: The Excel file is empty.")
    adal = None

if adal is not None:
    # Display the first 5 rows of the wind speed data
    print("\nFirst 5 rows of the Wind Speed DataFrame:")
    print(adal.head())
    
    # Display column names
    print("\nColumn names in the Wind Speed DataFrame:")
    print(adal.columns.tolist())
    
    # Display the total number of rows and columns
    print("\nShape of the Wind Speed DataFrame (rows, columns):")
    print(adal.shape)

    # Check for missing data
    print("\nNumber of missing values in each column of the Wind Speed DataFrame:")
    print(adal.isnull().sum())

# Step 3: Demonstrate DataFrame export using `to_csv`
if adal is not None:
    # Display a reference to the `to_csv` method
    print("\nReference to the 'to_csv' method of the Wind Speed DataFrame:")
    print(adal.to_csv)

    # Convert the Wind Speed DataFrame to a CSV string
    print("\nWind Speed DataFrame as a CSV-formatted string (without index):")
    print(adal.to_csv(index=False))

    # Save the DataFrame as a new CSV file (if desired)
    try:
        adal.to_csv(r"C:\Users\Bibek\Documents\project\data\Wind_Speed_Output.csv", index=False)
        print("\nWind Speed DataFrame successfully saved to 'Wind_Speed_Output.csv'")
    except Exception as e:
        print(f"Error: Failed to save the Wind Speed DataFrame to CSV. {e}")

# Step 4: Additional Operations and Insights (optional)
if afall is not None:
    # Describe statistical measures for numerical columns
    print("\nStatistical summary of the Rainfall DataFrame:")
    print(afall.describe())

    # Display unique values in a specific column (e.g., if the column 'Year' exists)
    if 'Year' in afall.columns:
        print("\nUnique years in the Rainfall DataFrame:")
        print(afall['Year'].unique())
    else:
        print("\nColumn 'Year' not found in the Rainfall DataFrame.")

if adal is not None:
    # Describe statistical measures for numerical columns in the wind speed data
    print("\nStatistical summary of the Wind Speed DataFrame:")
    print(adal.describe())

    # Check for duplicate rows in the Wind Speed DataFrame
    print("\nNumber of duplicate rows in the Wind Speed DataFrame:")
    print(adal.duplicated().sum())
