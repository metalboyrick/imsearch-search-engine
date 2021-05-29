from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .apps import SearchServiceConfig
from scipy.spatial import distance
from sentence_transformers import util
import json
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
  

from .models import *

def get_message(msg_content, status_code):
    return {'message': msg_content}, status_code

def compute_similarity(query):
    query_raw_tokens = query.split(" ")

    stop_words = set(stopwords.words('english')) 

    # loop through all labels
    labels = Label.objects.all()
    results = []
    debug = []
    token_embeddings = []

    # remove the stopwords
    query_tokens = [w for w in query_raw_tokens if not w in stop_words]

    print(query_tokens)

    for token in query_tokens:
        token_embeddings.append(SearchServiceConfig.sbert_model.encode(token))

    np_embeddings = np.array(token_embeddings)
    central_embedding = np_embeddings.mean(axis=0)
    
    for label in labels:
        label_embedding = json.loads(label.embedding)
        similarity = util.cos_sim(central_embedding , label_embedding)
        if similarity >= 0.475:
            res_entry = {
                'label_id': label.label_id,
                'label_name': label.label_name,
                'score': similarity[0].item()
            }
            results.append(res_entry)
            debug.append(label.label_name  + " " + str(similarity))


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

        # rank the results here

        # get the picture with the correct label from the database
        for value in similarities:
            search_contents = ImageLabels.objects.filter(label_id= value['label_id'])
            for image_labels in search_contents:
                res_data.append(image_labels.image_id.image_path)

    return JsonResponse(res_data, status=res_status, safe=False, headers={'Access-Control-Allow-Origin': '*'})

