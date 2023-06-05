import json

from django.http import HttpResponse
from django.shortcuts import render

from comment.models import Comment
from django.forms.models import model_to_dict
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def addComment(request):
    data = {}
    resp = {}

    if request.method == 'POST':
        body = request.body
        data = json.loads(body)
        productId = data['productId']
        content = data['content']
        comment = Comment(productId=productId, content=content, createdAt=timezone.now())
        comment.save()
        data = model_to_dict(comment)
        if data:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = data
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is not available.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Method is not allowed.'

    return HttpResponse(json.dumps(resp), content_type='application/json')


def listComment(request, productId):
    data = []
    resp = {}
    comments = Comment.objects.filter(productId=productId)
    for comment in comments.values():
        comment['createdAt'] = comment['createdAt'].isoformat()
        data.append(comment)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
