# Facility Location Problem Project

This project addresses the Facility Location Problem, which involves determining optimal facility locations to minimize costs and maximize coverage. The problem is tackled using geographic data for 128 U.S. and Canadian cities provided in a dataset (`miles.dat`). The project is divided into three phases, each focusing on a different aspect of the solution:

## Phase 1: Data Loading
- **Objective**: Parse the `miles.dat` file and store the data in structured lists:
  - `cityList`: Names of cities and states.
  - `coordList`: Latitude and longitude of cities.
  - `popList`: Population of cities.
  - `distanceList`: Pairwise distances between cities.
- **Functions**:
  - `loadData`: Reads and stores data in the lists.
  - `getCoordinates`: Retrieves latitude and longitude of a city.
  - `getPopulation`: Retrieves population of a city.
  - `getDistance`: Retrieves distance between two cities.
  - `nearbyCities`: Finds cities within a given radius.
  
## Phase 2: Facility Location Algorithm
- **Objective**: Implement a greedy algorithm to determine facility locations that minimize the number of facilities while ensuring every city is within a given radius (`r`) of a facility.
- **Function**:
  - `locateFacilities`: Returns a list of cities for facility placement based on the radius.

## Phase 3: Visualization
- **Objective**: Generate visual representations of the solution using KML files for visualization in Google Earth or Google Maps.
- **Function**:
  - `display`: Creates KML files showing facility locations and connections to served cities.
- **Deliverables**:
  - `visualization300.kml`: Facilities for a coverage radius of 300 miles.
  - `visualization800.kml`: Facilities for a coverage radius of 800 miles.

## Submission Files
1. `project1Phase1.py`: Phase 1 functions.
2. `project1Phase2.py`: Phase 2 functions.
3. `project1Phase3.py`: Phase 3 functions and main program.
4. `visualization300.kml`: Visualization for `r = 300`.
5. `visualization800.kml`: Visualization for `r = 800`.
