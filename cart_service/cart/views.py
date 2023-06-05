import json

import requests
from django.http import HttpResponse

from cart.models import Cart, CartItem
from django.forms.models import model_to_dict


def addToCart(request, customerId, productId):
    data = {}
    resp = {}
    try:
        userCart = Cart.objects.filter(customerId=customerId).values()[0]
        print(f'Cart id {userCart["id"]}')
        productPrice = getProductById(productId)['data']['price']
        print(f'Price {productPrice}')
        if userCart:
            cartItem = CartItem(productId=str(productId), cartId=userCart['id'], quantity=1, price=productPrice)

            cartItem.save()
            data = model_to_dict(cartItem)
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


def removeCart(request):
    data = {}
    resp = {}
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


def removeItemCart(request):
    data = {}
    resp = {}
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


def cartDetail(request, customerId):
    data = {}
    resp = {}
    products = []
    totalPrice = 0
    userCart = Cart.objects.filter(customerId=customerId).values()[0]
    cartItems = CartItem.objects.filter(cartId=userCart['id'])
    for item in cartItems.values():
        productId = item['productId']
        product = getProductById(productId)['data']
        products.append(product)
        totalPrice += item['price'] * item['quantity']

    if products:
        data['products'] = products
        data['total_price'] = totalPrice

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


def getProductById(productId):
    # Make a GET request to the API endpoint
    response = requests.get(f'http://127.0.0.1:6001/product/{productId}')

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()
        print(f'Data {data["status"]}')
    else:
        # Handle the error
        print(f'Request failed with status code {response.status_code}')
    return data
