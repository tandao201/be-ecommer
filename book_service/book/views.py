import json

from django.http import HttpResponse
from django.forms.models import model_to_dict

from book.models import Book


# Create your views here.

def getBookById(request, bookId):
    data = []
    resp = {}
    book = Book.objects.filter(id=bookId).values()[0]
    data = book
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


def getAllBooks(request):
    data = []
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
