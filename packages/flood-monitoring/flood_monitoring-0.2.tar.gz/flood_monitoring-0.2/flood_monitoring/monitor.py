import random
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class FloodMonitor:
    # root path for the available APIs
    root_pth = 'https://environment.data.gov.uk/flood-monitoring'

    # valid measurements
    valid_measurments = ('Water Level', 'Wind', 'Flow', 'Temperature', None)
    def __init__(self, town: str = None, parameterName: str = None, riverName: str = None, lat: float = None, long: float = None, dist: int = None):
        # check if the measurement is a string
        if type(parameterName) != str and parameterName is not None:
            raise ValueError('measurement must be a string')
        else:
            if parameterName not in self.valid_measurments:
                raise ValueError('Invalid measurement')
            else:
                # assign measurement appropriately
                if parameterName == 'Water Level':
                    self.measurement = 'Water Level'
                elif parameterName == 'Flow':
                    self.measurement = 'Flow'
                elif parameterName == 'Wind':
                    self.measurement = 'Wind'
                elif parameterName == 'Temperature':
                    self.measurement = 'Temperature'
                else:
                    self.measurement = None
        
        # check if the town is a string
        if type(town) != str and town is not None:
            raise ValueError('town must be a string')
        else:
            self.town = town

        # check if the river name is a string
        if type(riverName) != str and riverName is not None:
            raise ValueError('river name must be a string')
        else:
            self.river_name = riverName
        # set the latitude and longitude
        self.latitude = lat
        self.longitude = long

        # check if the distance is an integer
        if type(dist) != int and dist is not None:
            raise ValueError('distance must be an integer')
        else:
            self.distance = dist

        # dynamically set the parameters based on the given values, parameters set to None if all values are not provided
        params = {k: v for k, v in locals().items() if k != 'self' and v is not None}
        self.station_parameters = params if params else None
        
        # initialise parameters to be used in the API
        # self.station_parameters = {
        #     'parameterName': self.measurement,
        #     'town': self.town,
        #     'riverName': self.river_name,
        #     'lat': self.latitude,
        #     'long': self.longitude
        # }

        # get the current date 
        self.end_date = datetime.today().strftime('%Y-%m-%d')
        self.start_date = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
        # print(f'todays date is {self.current_date} and yesterday it was {self.yesterday_date}')
        self.reading_parameters = {'startdate': self.start_date,
                                   'enddate': self.end_date}
    
    def perform_monitoring(self, parameters: dict):
        # url for all the stations
        # self.stations_pth = os.path.join(self.root_pth, 'id/stations') # may not work on windows (works on linux)
        self.stations_pth = f"{self.root_pth}/id/stations"


        response = requests.get(self.stations_pth, params=parameters)
        # if request not good print error code
        if response.status_code != 200:
            raise ValueError(f'Error: {response.status_code}')
        else:
            data = response.json()
            # list of dictionaries 
            self.stations = data['items']
            # print a message if there are no stations based on the given parameters
            if len(self.stations) == 0:
                print('No stations found based on the given parameters')
            else:
                print(f'{len(self.stations)} Stations found based on the given parameters')
                # if there is only one station, get the readings for the station, otherwise select one at random
                if len(self.stations) == 1:                 
                    self.individual_station_pth = self.stations[0]['@id']
                
                else:
                    # select a random station
                    random_station = random.choice(self.stations)
                    self.individual_station_pth = random_station['@id']

                print(f'The selected station id is: {self.individual_station_pth}')

                # get all reading for selected station within last day
                readings_url = f'{self.individual_station_pth}/readings'


                readings_response = requests.get(readings_url, params=self.reading_parameters)

                reading_data = readings_response.json()

                # get list corresponding to items key, items is a list of dictionaries. Amongst other info each dictionary contains the readings(values) and date
                items = reading_data['items']
                # get the values and date (will be used for plotting)- dates are in the format '2021-07-01T00:00:00Z'.
                values = [item['value'] for item in items]
                dates = [item['dateTime'] for item in items]

                # make a pandas dataframe
                df = pd.DataFrame({'Date': dates, 'Value': values})
                print(df.head())

                # plot the values
                self._plot_line_graph(values)
                
                

    def _plot_line_graph(self, values: list):
        # plot the values 
        plt.plot(range(len(values)),values)
        plt.ylabel(self.measurement)
        plt.xlabel('Time (15 minute intervals)')
        plt.title(f'Readings from {self.start_date} to {self.end_date}')
        plt.show()


