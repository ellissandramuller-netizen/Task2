
import yaml 

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

    max_days = config["max_days_since_calibration"]
    output = config["output_file"]



   

