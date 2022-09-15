import requests
import json


def get_fb_posts_by_date(url):
    data = requests.get(url)
    response = dict()  # hold response info
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli
    return response  # get and return content


def get_ig_posts_by_date(url):
    data = requests.get(url)
    response = dict()  # hold response info
    response['json_data'] = json.loads(data.content)  # response data from the api
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)  # pretty print for cli
    return response  # get and return content
