# Weathervane

Agent to periodically collect weather data from the Darksky API (https://darksky.net/dev/docs), store in datastore. When user accesses our endpoint, we query the datastore, pull data, and graph in D3. Compares weather prediction from midnight each day to the actual weather that occurs that day.



### Requirements:
- Python 3
- Pip3
- Postgres (postgres user must not require a password)
  - under MacOSX, you'll want to install Homebrew (https://brew.sh/),
  - then `brew install postgresql`


# Run Directions


1. Navigate to weathervane:
   `cd failure_enthusiasts/projects/weathervane`

2. Copy `variables.sh` to `weathervane/`
    a. `python3 -m venv venv`

3. Activate the virtualEnv - `. venv/bin/activate`

4. Tab 2: Start flask app! `./run_flask.sh`

5. Go to `http://0.0.0.0:3030/` (or set local port location - flask will report the URL at runtime)

For styling:
https://developer.snapappointments.com/bootstrap-select/examples/
