from scrape import get_price_avg
import json
from datetime import datetime

thinkpad_data = []

"""Instead of using a regex to filter unwanted models, we can simply use ebay's
built in search operators in the second argument"""

model_and_search = {
    "X230": "X230  -X230S",
    "T430":"Thinkpad T430 -T430S",
    "T440":"Thinkpad T440 -T440S",
    "T480":"T480 -T480S"
}

# def refine_search(arr): # In the future will take an array of strings to include in search, such as unwanted items i.e battery, keyboard, charger.
#     pass

for k, v in model_and_search.items():
    val = get_price_avg(k,v)
    thinkpad_data.append(val)

print(str(thinkpad_data))

current_date = datetime.now()
json_date = current_date.isoformat()
print(json_date)

json_data = json.dumps(thinkpad_data,json_date)

with open('py_data.json', 'w') as file:
    file.write(json_data)
