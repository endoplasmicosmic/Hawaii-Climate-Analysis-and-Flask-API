# Import the dependencies.
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Print all of the classes mapped to the Base
Base.classes.keys()

# Assign the measurement class to a variable called `Measurement` and the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

# Find the most recent date in the data set.
most_recent_date = session.query(func.max(Measurement.date)).first()[0]
print(f"Most recent date: {most_recent_date}")

# Close the session
session.close()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define the home route
@app.route("/")
def welcome():
    return (
        f"<h3>Welcome to the Hawaii Climate Analysis API! </h3>"
        f"Available Routes: <br/>" 
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MM-DD-YY. </p>"
    )
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a session
    session = Session(engine)
    
    # Calculate the date one year from the last date in data set.
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
                         filter(Measurement.date >= one_year_ago).\
                         order_by(Measurement.date).all()

    session.close()

    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

    return jsonify(precipitation_dict)
#################################################
@app.route("/api/v1.0/stations")
def stations():
    # Create a session
    session = Session(engine)
    
    # Perform a query to retrieve all stations
    stations_data = session.query(Station.station).all()
    
    session.close()

    # Convert the query results to a list
    stations_list = [station[0] for station in stations_data]

    return jsonify(stations_list)
#################################################
@app.route("/api/v1.0/tobs")
def tobs():
    # Create a session
    session = Session(engine)
    
    # Calculate the date one year from the last date in data set.
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the dates and temperature observations of the most active station for the last year
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
               filter(Measurement.station == 'USC00519281').\
               filter(Measurement.date >= one_year_ago).all()
    
    session.close()

    # Convert the query results to a list
    tobs_list = [{date: tobs} for date, tobs in tobs_data]

    return jsonify(tobs_list)
#################################################
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def temperature_range(start, end=None):
    # Create a session
    session = Session(engine)
    
    # If no end date is provided, query the data for the range starting from the start date
    if not end:
        results = session.query(func.min(Measurement.tobs), 
                                func.avg(Measurement.tobs), 
                                func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).all()
    else:
        results = session.query(func.min(Measurement.tobs), 
                                func.avg(Measurement.tobs), 
                                func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).\
                  filter(Measurement.date <= end).all()
    
    session.close()

    # Convert the query results to a dictionary
    temp_dict = {
        "T.MIN": results[0][0],
        "T.AVG": results[0][1],
        "T.MAX": results[0][2]
    }

    return jsonify(temp_dict)

if __name__ == '__main__':
    app.run(debug=True)


