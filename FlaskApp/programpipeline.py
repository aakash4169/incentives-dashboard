import subprocess as sp
import os
from pathlib import Path
from jsonify import jsonifyPrograms
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticIndexer import indexJson
import json


def runPipeline(): 

    try:
        sp.run(args=['scrapy', 'crawl', 'StateIncentivesSpider', '-t', 'csv', '-o', 'newprogramdata.csv', '--nolog'])

        if Path('programdata.csv').is_file():
            os.remove('programdata.csv')
        os.rename('newprogramdata.csv', 'programdata.csv')

        jsonifyPrograms()

        indexJson()

    except Exception as e:
        print('An error has occurred :(')
        print(type(e))
        print(e)