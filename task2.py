import json

import pandas as pd
import yaml

# Åpne og hente ut relevante verdier fra config.yml
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

    max_days = config["max_days_since_calibration"]
    output = config["output_file"]

# Lese kalibrasjons data og sensor data som panda dataframes
calib_data = pd.read_csv('calibrations.csv')
sensor_data = pd.read_excel('sensors.xlsx')

# Slå sammen sensor data og kalibrasjonsdata basert på sensor-ID
merged_data = pd.merge(
    sensor_data,
    calib_data,
    on="sensor_id"
)

# Hente ut sensorene som har overskredet maks antall dager siden kalibrering
overdue_data = merged_data[merged_data["days_since_calibration"] > max_days]

# Konvertere utgåtte sensorer til en liste med dictionaries for JSON-eksport
overdue_sensors = overdue_data.to_dict(orient="records")

# Skrive relevante sensorer og tilhørende data til JSON-fil
with open(output, 'w') as file:
    json.dump(overdue_sensors, file, indent=2)