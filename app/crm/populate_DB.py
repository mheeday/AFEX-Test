import requests
from .models import Client
from django.db import IntegrityError
#from background_task import background

#@background(schedule=0)
def populate_client_model():
    try:
        data_response = requests.get('https://62c2c06cff594c656764970a.mockapi.io/users')
        if data_response.status_code != 200:
            raise Exception 

        json_data = data_response.json()

        if json_data['message'] != 'successful':
            raise Exception
        
        for data in json_data['data']:
            new_client = Client(
                cid = data['cid'], 
                first_name = data['first_name'], 
                last_name = data['last_name'],
                country_code = data['country_code'], 
                email = data['email'], 
                address = data['address'], 
                phone = data['phone'])
            
            print('no')   

            try:
                new_client.save()
            except IntegrityError:
                print('CID Exist')
                continue
    except:
        pass