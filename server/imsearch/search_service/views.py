from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .models import *

def get_message(msg_content, status_code):
    return {'message': msg_content}, status_code

# Create your views here.
def search(request):
    res_data = {}
    res_status = 200

    if request.method != 'GET':
        res_data, res_status = get_message("invalid request", 400)
    else:
        res_data = []

        search_query = request.GET["query"]

        # get the picture with the correct label from the database
        search_contents = ImageLabels.objects.filter(label_id__label_name__icontains = search_query)

        for image_labels in search_contents:
            res_data.append(image_labels.image_id.image_path)


    return JsonResponse(res_data, status=res_status, safe=False, headers={'Access-Control-Allow-Origin': '*'})