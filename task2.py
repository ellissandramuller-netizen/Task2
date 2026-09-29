
import yaml 
import pandas as pd

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

