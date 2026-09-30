
import yaml 
import pandas as pd
import json


with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

    max_days = config["max_days_since_calibration"]
    output = config["output_file"]

calib_data = pd.read_csv('calibrations.csv')
sensor_data = pd.read_excel('sensors.xlsx')

merged_data = pd.merge(
    sensor_data,
    calib_data,
    on="sensor_id"
)

overdue_data = merged_data[merged_data["days_since_calibration"] > max_days]

overdue_sensors = overdue_data.to_dict(orient="records")

with open(output, 'w') as file:
    json.dump(overdue_sensors, file, indent=2)
  