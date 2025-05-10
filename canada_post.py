
import json
import sys
import os


headers = {
	"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0"
}

tracking_id = sys.argv[1]

url = f"https://www.canadapost-postescanada.ca/track-reperage/rs/track/json/package/{tracking_id}/detail"

print(url)

## issue with requests.get being blocked!! 
response = os.popen(f"curl {url}").read()

json_response = json.loads(response)

events = json_response['events']

for event in events:
    description = event['descEn']
    datetime = event['datetime']
    date = datetime['date']
    time = datetime['time']
    print(date,time,":",description)
