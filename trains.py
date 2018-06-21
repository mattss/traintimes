import sys

import requests

api_url = 'https://fcc.transportapi.com/v3/uk/train/station/{source}/live.json?limit=10&calling_at={destination}'

try:
    source, destination = sys.argv[1:]
except ValueError:
    print('Please provide a source and destination')
    sys.exit(1)

result = requests.get(api_url.format(
    source=source,
    destination=destination,
))

data = result.json()
print(data['station_name'])

for result in data['departures']['all']:
    print('{aimed_departure_time} // {status} - {destination_name}'.format(**result))
