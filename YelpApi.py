import requests
import random

business_id = 'kApVYIWwlriVK1pqPVrOPg'

API_KEY = '_5qOZHWTK4tjf0PzbSumf7l0oOgq6ZNl0cP04_zXtijrwRs-hQqs3VHUW69ok4JC2YoIPhyUOyq7tE-8TldNdfyhT8HltpV9KqCeG8jArab9rZdDxGthP--PAvY3X3Yx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define parameters
PARAMETERS = {'term': 'restaurant',
    'limit': 50,
    'radius': 5000,
    #'offset': 50,
    'location': 'augusta'}

#Make a request to the yelp API
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

#convert the JSON string to a Dictionary
business_data = response.json()

def business_search_results():
    biz_list = []
    for biz in business_data['businesses']:
        biz_list.append(biz['name'])
    return random.choice(biz_list)

#print(business_search_results())