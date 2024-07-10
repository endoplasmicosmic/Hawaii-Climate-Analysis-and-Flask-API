# Hawaii Climate Analysis and Flask API

## Background

This project focuses on analyzing climate data for Honolulu, Hawaii. The analysis involves querying and visualizing the data, and creating a Flask API based on these queries.

## Project Structure

### Files

- `climate_starter.ipynb`: Jupyter Notebook containing the climate data analysis.
- `app.py`: Flask API to serve the analyzed data.
- `hawaii.sqlite`: SQLite database containing the climate data.
- `hawaii_measurements.csv`: CSV file with measurement data.
- `hawaii_stations.csv`: CSV file with station data.

### Data Analysis

#### Precipitation Analysis

The precipitation analysis involves:
- Finding the most recent date in the dataset.
- Retrieving the last 12 months of precipitation data.
- Plotting the results.

![Precipitation Analysis](SurfsUp/precipitation_analysis.png)

#### Station Analysis

The station analysis involves:
- Calculating the total number of stations.
- Listing the stations and their observation counts in descending order.
- Finding the minimum, maximum, and average temperatures for the most active station.
- Plotting a histogram of the last 12 months of temperature observation data.

![Temperature Observation Histogram](SurfsUp/temperature_observation_histogram.png)

## Flask API

The Flask API serves the climate data through various routes.

### Available Routes

- `/api/v1.0/precipitation`: Returns the date and precipitation data for the last year.
- `/api/v1.0/stations`: Returns a list of all stations.
- `/api/v1.0/tobs`: Returns the temperature observations for the most active station for the last year.
- `/api/v1.0/temp/<start>`: Returns the minimum, average, and maximum temperatures from the start date to the end of the dataset.
- `/api/v1.0/temp/<start>/<end>`: Returns the minimum, average, and maximum temperatures for the specified start and end date range.

### Example Queries

#### Precipitation Data

```sh
curl http://127.0.0.1:5000/api/v1.0/precipitation
curl http://127.0.0.1:5000/api/v1.0/stations
curl http://127.0.0.1:5000/api/v1.0/tobs
curl http://127.0.0.1:5000/api/v1.0/temp/20170101
curl http://127.0.0.1:5000/api/v1.0/temp/20170101/20171231

### Additional Info

- The various graphs and charts created from analysis can be viewed in the `graph_visuals` folder of this repository.
- The CSV and SQLite datasets can be viewed in the `Resources` folder of this repository.
- The Python code can be viewed in the `climate.ipynb` notebook and `app.py` script in this repository.

### Sources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
