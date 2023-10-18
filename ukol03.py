import json

with open('body.json', encoding = 'utf-8') as file:
    prospech = json.load(file)

slovni_prospech = {}

for key, value in prospech.items():
    if value >= 60:
        slovni_prospech[key] = 'pass'
    else:
        slovni_prospech[key]= 'fail'

print(slovni_prospech)

with open('prospech.json', mode = "w", encoding= 'utf-8') as file:
    json.dump(slovni_prospech, file, ensure_ascii = False)
    
