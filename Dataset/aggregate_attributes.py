import pandas as pd

# Load your CSV data into a pandas DataFrame
df = pd.read_csv("Global_Weather_Repository_Cleaned.csv")

# Define the columns you want to aggregate
columns_to_aggregate = [
    "temperature_celsius",
    "temperature_fahrenheit",
    "wind_mph",
    "wind_kph",
    "pressure_mb",
    "pressure_in",
    "precip_mm",
    "precip_in",
    "humidity",
    "cloud",
    "feels_like_celsius",
    "feels_like_fahrenheit",
    "visibility_km",
    "visibility_miles",
    "uv_index",
    "gust_mph",
    "gust_kph",
    "air_quality_Carbon_Monoxide",
    "air_quality_Ozone",
    "air_quality_Nitrogen_dioxide",
    "air_quality_Sulphur_dioxide",
    "air_quality_PM2.5",
    "air_quality_PM10",
    "air_quality_us-epa-index",
    "air_quality_gb-defra-index",
]

# Group by 'country' and 'continent', and calculate the mean for each specified column
aggregated_df = (
    df.groupby(["country", "continent"])[columns_to_aggregate].mean().reset_index()
)

aggregated_df[
    [
        "temperature_celsius",
        "temperature_fahrenheit",
        "wind_mph",
        "wind_kph",
        "pressure_mb",
        "pressure_in",
        "precip_mm",
        "precip_in",
        "humidity",
        "cloud",
        "feels_like_celsius",
        "feels_like_fahrenheit",
        "visibility_km",
        "visibility_miles",
        "uv_index",
        "gust_mph",
        "gust_kph",
        "air_quality_Carbon_Monoxide",
        "air_quality_Ozone",
        "air_quality_Nitrogen_dioxide",
        "air_quality_Sulphur_dioxide",
        "air_quality_PM2.5",
        "air_quality_PM10",
        "air_quality_us-epa-index",
        "air_quality_gb-defra-index",
    ]
] = aggregated_df[
    [
        "temperature_celsius",
        "temperature_fahrenheit",
        "wind_mph",
        "wind_kph",
        "pressure_mb",
        "pressure_in",
        "precip_mm",
        "precip_in",
        "humidity",
        "cloud",
        "feels_like_celsius",
        "feels_like_fahrenheit",
        "visibility_km",
        "visibility_miles",
        "uv_index",
        "gust_mph",
        "gust_kph",
        "air_quality_Carbon_Monoxide",
        "air_quality_Ozone",
        "air_quality_Nitrogen_dioxide",
        "air_quality_Sulphur_dioxide",
        "air_quality_PM2.5",
        "air_quality_PM10",
        "air_quality_us-epa-index",
        "air_quality_gb-defra-index",
    ]
].round(
    2
)

# Now, filtered_df contains only rows where "wind_direction" is one of the specified values
# Save the aggregated data to a new CSV file
aggregated_df.to_csv("aggregated_temperature.csv", index=False)
