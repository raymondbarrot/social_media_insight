import requests
import json
import snscrape.modules.twitter as sntwitter
import twint
import datetime


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


def get_twitter_posts_by_date():
    query = "(from:DTIRegion4A) until:2022-10-01 since:2022-09-01"
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        print(vars(tweet))





