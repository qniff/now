# Now
A terminal utility to check time in different countries.

## Installation
* ```git clone https://github.com/qniff/now```
* ```cd now```
* If you don't want to install dependencies globally ```source venv/bin/activate```
* Otherwise ```pip install --user --requirement requirements.txt```
* Set custom alias for convenience (E.g ```alias now='python ~/Scripts/now/now.py'```)

## Usage
* ```python now.py``` - Current time and time zone information
* ```python now.py ca``` - Time in the country by country index
* ```python now.py japan``` - Time in the country by country name
* ```python now.py -l``` - List all available countries
* ```python now.py -h``` - Help page