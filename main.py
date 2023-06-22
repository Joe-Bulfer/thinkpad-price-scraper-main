from scrape import get_price_avg

thinkpad_data = []

"""Instead of using a regex to filter unwanted models, we can simply use ebay's
built in search operators in the second argument"""

val = get_price_avg("T430","T430 -T430s")
thinkpad_data.append(val)

val = get_price_avg("T480S","T480 -T480S")
thinkpad_data.append(val)

val = get_price_avg("X230","X230 -X230S")
thinkpad_data.append(val)

print(str(thinkpad_data))

# json_data = json.dumps(price_avg)

# with open('py_data.json', 'w') as file:
#     file.write(json_data)
#    thinkpad_data.append({"model": model,"price_avg": price_avg})