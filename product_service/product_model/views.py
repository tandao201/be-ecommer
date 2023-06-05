# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details
from django.forms.models import model_to_dict


@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')


def getProductById(request, product_id):
    data = []
    resp = {}
    # This will fetch the data from the database.
    try:
        prodata = product_details.objects.get(id=product_id)
        if prodata:
            data = model_to_dict(prodata)
        # If data is available then it returns the data.
        if data:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is not available.'
    except:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')


def getBookById(request, bookId):
    data = []
    resp = {}
    # This will fetch the data from the database.
    try:
        book = requestBookApi(bookId)['data']
        data = book
        if data:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is not available.'
    except:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')


def requestBookApi(bookId):
    # Make a GET request to the API endpoint
    response = requests.get(f'http://127.0.0.1:9004/book/{bookId}')

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()
        print(f'Data {data["status"]}')
    else:
        # Handle the error
        print(f'Request failed with status code {response.status_code}')
    return data
