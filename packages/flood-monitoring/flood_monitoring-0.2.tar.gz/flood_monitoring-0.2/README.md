# Flood Monitoring
This project uses the [Real Time flood-monitoring API](https://environment.data.gov.uk/flood-monitoring/doc/reference) 
to monitor flood information at specific measurement stations.

## Installation
In a new conda environment, you can install the package via pip:

```pip install flood-monitoring```

## Example Usage
To select an individual measurement station, users can specify:
1. The Town name, 
2. The River name, 
3. The specific measurement of interest (water level, water flow rate, wind direction and speed, or temperature).
4. The specific latitude and longitude coordinates of the region of interest. 
5. A distance d (in kilometers) of all stations falling within d km of the specified latitude and longitude. 

For further details on the available options, run:

```python -m flood_monitoring.main  --help```

For example, running the following command: 

```python -m flood_monitoring.main  --latitude 51.874767 --longitude -1.740083 --measurement 'Water Level'``` 

gives the following output:

```The selected station id is: http://environment.data.gov.uk/flood-monitoring/id/stations/1029TH```

and displays the first five rows of readings from the particular station over the last 24 hours:

```
                Date     Value
0  2025-03-09T00:00:00Z -0.163
1  2025-03-09T00:15:00Z -0.163
2  2025-03-09T00:30:00Z -0.165
3  2025-03-09T00:45:00Z -0.163
4  2025-03-09T01:00:00Z -0.163
```

as well as a line graph of that station's readings over the last 24 hours:

![line graph](examples/example_line_graph.png)