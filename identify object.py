### Identifying the object in orbit using TLEs

# Importing the necessary libraries
from satellitetle import fetch  # "pip install satellitetle"
from difflib import SequenceMatcher as sm   # "pip install python-Levenshtein"
from tletools import TLE  # "pip install TLE-tools"

# Fetching the TLE data from Celestrak
tleData = fetch()

# Function to find the closest matching satellite using the TLEs
def findClosestSatellite(tleInput):
    bestMatch = None
    bestSimilarity = 0

    for satellite in tleData:
        similarity = sm(None, satellite.name, tleInput).ratio()
        if similarity > bestSimilarity:
            bestSimilarity = similarity
            bestMatch = satellite
    
    return bestMatch, bestSimilarity

# Function to interpret and present TLE data using TLE-tools
def interpretTLE(tleString):
    tle = TLE.from_string(tleString)

    interpretation = {
        "Satellite Number": tle.satellite_number,
        "Classification": tle.classification,
        "International Designator": tle.int_desig,
        "Element Set Epoch": tle.epoch,
        "Element Set Epoch Year": tle.epochyr,
        "Element Set Epoch Day": tle.epochdays,
        "First Time Derivative of the Mean Motion": tle.dndt,
        "Second Time Derivative of Mean Motion (decimal point assumed)": tle.d2ndt2,
        "B* Drag Term": tle.bstar,
        "Element Set Type": tle.elnum,
        "Element Number": tle.revnum,

        "Inclination": tle.inclination,
        "Right Ascension of the Ascending Node": tle.raan,
        "Eccentricity": tle.eccentricity,
        "Argument of Perigee": tle.argp,
        "Mean Anomaly": tle.mean_anomaly,
        "Mean Motion": tle.mean_motion,
        "Orbit Number at Epoch": tle.orbit
    }

    return interpretation

# Example individual values for subset of line 2


# Find the closest matching satellite
result, similarity = findClosestSatellite(tleInput)

if result:
    print("Best match: ", result.name)
    print(f"similarity: {similarity*100:.2f}%")

    # Interpret the TLE data
    interpretation = interpretTLE(result.tle)
    for key, value in interpretation.items():
        print(f"{key}: {value}")

else:
    print("No match found")