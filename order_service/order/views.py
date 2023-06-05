import json

import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def order(request, customerId):
    data = {}
    resp = {}
    userCart = getCartById(customerId)
    if userCart:
        data['products'] = userCart['products']
        data['shipment'] = []
        data['payment'] = []
        data['totalPrice'] = userCart['total_price']

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

def getCartById(customerId):
    # Make a GET request to the API endpoint
    response = requests.get(f'http://127.0.0.1:9001/cart-detail/{customerId}')

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()
        print(f'Data {data["status"]}')
        return data['data']
    else:
        # Handle the error
        print(f'Request failed with status code {response.status_code}')
    return []
