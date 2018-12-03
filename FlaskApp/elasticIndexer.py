from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

def indexJson():
    es = Elasticsearch()

    es.indices.delete(index='program', ignore=[400, 404])

    es.indices.create(index='program', ignore=[400, 404])
    
    with open ('programs_formatted.json') as json_file:
        body=json_file.readlines()
        
    bulk(es, actions=body, index='program', doc_type='_doc',)