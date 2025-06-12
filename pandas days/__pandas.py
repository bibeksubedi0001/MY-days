import pandas as pd

# Create a DataFrame with the updated design
data = {
    "Date": [
        "1/1/2019 0:00", "1/1/2019 1:00", "1/1/2019 2:00", "1/1/2019 3:00",
        "1/1/2019 4:00", "1/1/2019 5:00", "1/1/2019 6:00", "1/1/2019 7:00",
        "1/1/2019 8:00", "1/1/2019 9:00"
    ],
    "Precipitation": [0.5, 20.5, 0.6, 23.4, 0.0, None, 15.7, 30.0, 0.0, 18.5],
    "Temperature": [22.0, 21.8, 21.5, 21.2, 21.0, 20.8, 22.3, 23.0, 22.0, 21.9],
    "name": ["Bibek S", "Raj B", "Kumar", "Bibek", "Priya", "Sophia", "John", "Bibek C", "David", "Sara"],
    "Station": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Humidity": [65, 70, 75, 68, 80, 85, 78, 60, 55, 62],
    "WindSpeed": [5.2, 3.8, 2.4, 6.0, 1.5, 0.0, 4.6, 8.2, 2.1, 3.0],
    "Category": ["Light", "Moderate", "Light", "Heavy", "None", "None", "Moderate", "Heavy", "None", "Moderate"]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
file_path = r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv"
df.to_csv(file_path, index=False)

file_path
