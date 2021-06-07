from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .apps import SearchServiceConfig
from scipy.spatial import distance
from sentence_transformers import util
import json
import numpy as np

from .models import *


STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
              "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def get_message(msg_content, status_code):
    return {'message': msg_content}, status_code


def compute_similarity(query):
    query_raw_tokens = query.split(" ")

    # loop through all labels
    labels = Label.objects.all()
    results = []
    debug = []
    token_embeddings = []

    # remove the stopwords
    query_tokens = [w for w in query_raw_tokens if not w.lower() in STOP_WORDS]
    print(query_tokens)

    for token in query_tokens:
        token_embeddings.append(SearchServiceConfig.sbert_model.encode(token))

    np_embeddings = np.array(token_embeddings)
    central_embedding = np_embeddings.mean(axis=0)

    for label in labels:
        label_embedding = json.loads(label.embedding)
        similarity = util.cos_sim(central_embedding, label_embedding)
        if similarity >= 0.475:
            res_entry = {
                'label_id': label.label_id,
                'label_name': label.label_name,
                'score': similarity[0].item()
            }
            results.append(res_entry)
            debug.append(label.label_name + " " + str(similarity))

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
        similarities.sort(reverse=True, key=(lambda obj: obj['score']))

        # get the picture with the correct label from the database
        count = 0
        for value in similarities:
            search_contents = ImageLabels.objects.filter(
                label_id=value['label_id'])
            for image_labels in search_contents:
                if count <= 100:
                    res_data.append(image_labels.image_id.image_path)
                    count += 1
                else:
                    break

    res_headers = {
        'Access-Control-Allow-Origin': '*',
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
        "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    }

    return JsonResponse(res_data, status=res_status, safe=False, headers=res_headers)
