import json

apis_in_json = open('apis.json')
json_data = json.load(apis_in_json)
apis_requested = open('input.txt')
acls = []

for j in apis_requested:
    for i in json_data:
        if j.split() == i['uris'].split():
            acls.append(i['plugins'][3]['config.whitelist'][0])

print(sorted(set(acls)))
apis_in_json.close()
apis_requested.close()

