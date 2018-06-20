import requests

api_url = 'https://fcc.transportapi.com/v3/uk/train/station/BRI/live.json?limit=10&calling_at=BPW'

result = requests.get(api_url)

data = result.json()
print(data['station_name'])

for result in data['departures']['all']:
    print('{aimed_departure_time} // {status} - {destination_name}'.format(**result))
