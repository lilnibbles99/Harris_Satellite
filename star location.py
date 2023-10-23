
import requests
import json

R = requests.post('http://nova.astrometry.net/api/login', data={'request-json': json.dumps({"apikey": "lhgseqmicalgnwvs"})})

#https://astrometry.net/doc/net/api.html
#done through api (sadly)

