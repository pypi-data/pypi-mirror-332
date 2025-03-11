import argparse
from flood_monitoring.monitor import FloodMonitor

def check_valid_lat(value: float):
    # try to convert the value to a float
    try:
        value = float(value)
    except ValueError:
        raise ValueError('Latitude must be a float')
    
    # check if the value is between -90 and 90
    if value < -90 or value > 90:
        raise ValueError('Latitude must be between -90 and 90')
    
    return value

def check_valid_lon(value: float):
    # try to convert the value to a float
    try:
        value = float(value)
    except ValueError:
        raise ValueError('Longitude must be a float')
    
    # check if the value is between -180 and 180
    if value < -180 or value > 180:
        raise ValueError('Longitude must be between -180 and 180')
    
    return value

def main(args):
    # flood monitor agruments
    flood_monitor_args = {
        'town': args.town,
        'parameterName': args.measurement,
        'riverName': args.river_name,
        'lat': args.latitude,
        'long': args.longitude,
        'dist': args.distance
    }

    # make an instance of the FloodMonitor class
    fm = FloodMonitor(**flood_monitor_args)

    # flood monitoring 
    fm.perform_monitoring(fm.station_parameters)

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    # arguments to provide control over measurement station
    parser.add_argument('--town', type=str, help='The town to monitor')
    parser.add_argument('--measurement', type=str, choices=['Water Level', 'Wind', 'Flow', 'Temperature'], help='The measurement to monitor')
    parser.add_argument('--river_name', type=str, help='The river name')
    parser.add_argument('--latitude', type=check_valid_lat, help='The latitude of the town, valid values are between -90 and 90')
    parser.add_argument('--longitude', type=check_valid_lon, help='The longitude of the town, valid values are between -180 and 180')
    parser.add_argument('--distance', type=int, help='return stations within the specified distance of the given latitude and longitude in km')
    args = parser.parse_args()

    main(args)