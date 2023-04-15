#from donor.models import Wilaya,Daiira
import requests
import json

api_response = requests.get('https://www.linatabara3.com/api/dairas/1')

#for i in range(1,59):

    o = 1
    for i in range(1,59):
        api_response = requests.get(f'https://www.linatabara3.com/api/dairas/{i}')
        data = api_response.text
        parse_json = json.loads(data)
        #print(parse_json)
        for j in parse_json:
            Daiira(
                number = o,
                name = j['name'],
                wilaya_n = i
            ).save()
            o += 1
            
