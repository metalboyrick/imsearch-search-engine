from django.apps import AppConfig
from sentence_transformers import SentenceTransformer
import nltk


class SearchServiceConfig(AppConfig):
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search_service'
    nltk.download('stopwords')
    sbert_model = SentenceTransformer('average_word_embeddings_glove.6B.300d')

