from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .apps import SearchServiceConfig
from scipy.spatial import distance
from sentence_transformers import util
import json

from .models import *

def get_message(msg_content, status_code):
    return {'message': msg_content}, status_code

def compute_similarity(query):
    query_embedding = SearchServiceConfig.sbert_model.encode(query)
    
    # loop through all labels
    labels = Label.objects.all()
    results = []
    debug = []
    for label in labels:
        label_embedding = json.loads(label.embedding)
        similarity = util.cos_sim(query_embedding, label_embedding)
        if similarity >= 0.40:
            results.append(label.label_id)
            debug.append(label.label_name)


    print(debug)
    
    return results

# Create your views here.
def search(request):
    res_data = {}
    res_status = 200

    if request.method != 'GET':
        res_data, res_status = get_message("invalid request", 400)
    else:
        res_data = []

        search_query = request.GET["query"]
        similarities = compute_similarity(search_query)

        # get the picture with the correct label from the database
        for value in similarities:
            search_contents = ImageLabels.objects.filter(label_id= value)
            for image_labels in search_contents:
                res_data.append(image_labels.image_id.image_path)

    return JsonResponse(res_data, status=res_status, safe=False, headers={'Access-Control-Allow-Origin': '*'})

