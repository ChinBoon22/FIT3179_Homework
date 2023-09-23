import pandas as pd

# Load your CSV data into a pandas DataFrame
df = pd.read_csv('Global_Weather_Repository_Cleaned.csv')

# Define the columns you want to aggregate
columns_to_aggregate = ['wind_mph', 'wind_kph']

# Group by 'country' and 'continent', and calculate the mean for each specified column
aggregated_df = df.groupby(['continent', "wind_direction"])[
    columns_to_aggregate].mean().reset_index()

# Define the values you want to keep in the "wind_direction" column
specified_wind_directions = ['N', 'W', 'E', 'S', 'NE', 'NW', 'SW', 'SE']

# Filter the DataFrame to keep only rows where "wind_direction" is in the specified values
filtered_df = aggregated_df[aggregated_df['wind_direction'].isin(
    specified_wind_directions)]

filtered_df[['wind_mph', 'wind_kph']] = filtered_df[[
    'wind_mph', 'wind_kph']].round(2)

# Now, filtered_df contains only rows where "wind_direction" is one of the specified values
# Save the aggregated data to a new CSV file
filtered_df.to_csv('aggregated_data_with_wind.csv', index=False)
