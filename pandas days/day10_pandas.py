import pandas as pd

# Load the dataset
aa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Create a copy of the original dataframe
ab = aa.copy()

# Extract the first name from the 'name' column
ab["First_Name"] = ab["name"].str.split(" ").str[0]

# Query the dataframe for rows where First_Name is 'Bibek'
print(ab.query("First_Name == 'Bibek'"))

# Convert the 'Date' column to datetime format
ab["DATE_NEW"] = pd.to_datetime(ab["Date"])

# Display the info about the dataframe
print(ab.info())

# Show the modified dataframe
print(ab)

# Extract the year from 'DATE_NEW' and create a new column 'born_year'
ab["born_year"] = ab["DATE_NEW"].dt.year

# Print the 'born_year' column
print(ab["born_year"])

# Create categories based on 'Humidity'
ab["categories"] = ab["Humidity"].apply(
    lambda x: "Best" if x < 65 else ("Better" if x < 80 else "Moderate")
)

# Print the updated dataframe with categories
print(ab)

# Function to determine if outdoor games are possible based on weather conditions
def determine_game(row):
    if row['Precipitation'] < 0.8 and row['Temperature'] < 22:
        return "good_to_play_outdoor_game"
    elif row['Precipitation'] < 18.8 and row['Temperature'] < 23:
        return "football?OK"
    else:
        return "no_game_please"

# Apply the function to each row and create a new 'games' column
ab["games"] = ab.apply(determine_game, axis=1)

# Print the final dataframe with the 'games' column
print(ab)

