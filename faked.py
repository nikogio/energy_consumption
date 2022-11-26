
from faker import Faker 
import json            # To create a json file                 
import numpy as np
import pandas as pd
import requests

fake = Faker('da_DK')
def create_data(x): 
  
    # dictionary 
    friends_data ={} 
    for i in range(0, x): 
        
        friends_data[i]={} 
        friends_data[i]['name']= fake.name() 
        friends_data[i]['address']= fake.address() 
        friends_data[i]['city']= fake.city() 
        friends_data[i]['consumption']= fake.random_int(min=0, max=7000)
        friends_data[i]['range_0_4']= fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=0.2, max_value=0.6)
        friends_data[i]['range_4_8']= fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=0.5, max_value=1.1)
        friends_data[i]['range_8_12']= fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=2.1, max_value=2.8)
        friends_data[i]['range_12_16']= fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=1.3, max_value=2.0)
        friends_data[i]['range_16_20']= fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=5.0, max_value=5.8)
        friends_data[i]['range_20_24']= fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=1.4, max_value=2.0)
        friends_data[i]['from_date'] = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None)    
    return friends_data
    
friends = create_data(10)
pd.DataFrame.from_dict(friends)

print(friends)
response = requests.get(
    url='https://api.energidataservice.dk/dataset/DatahubPricelist?offset=0&sort=ValidFrom%20DESC&timezone=dk&limit=30&ChargeType=D03&columns=ChargeOwner,Description,ValidFrom,ValidTo,Price1,Price2,Price3,Price4,Price5,Price6,Price7,Price8,Price9,Price10,Price11,Price12,Price13,Price14,Price15,Price16,Price17,Price18,Price19,Price20,Price21,Price22,Price23,Price24&limit=5')

result = response.json()

for k, v in result.items():
    print(k, v)

records = result.get('records', [])
                                           
print('records:')
for record in records:
    print(' ', record)