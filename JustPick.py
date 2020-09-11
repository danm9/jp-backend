from YelpApi import business_search_results
import random

#print(business_search_results())

def just_pick():
    random_pick = random.choice(business_search_results())
    return random_pick

#print(random_pick)