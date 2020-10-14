import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['TATUM_PATH'])
API_KEY = os.environ['API_KEY']

def create_new_subcription(body_params):
    validator.create_new_subcription(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/subscription", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def list_all_active_subscriptions(query_params):
    validator.page_size_query_params(query_params)
    headers = {'x-api-key': API_KEY}

    if len(query_params) != 1:
        conn.request("GET", "/v3/subscription?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers)
    else: 
        conn.request("GET", "/v3/subscription?pageSize={}".format(query_params['pageSize']), headers=headers)


#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def cancel_existing_subscription(path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("DELETE", "/v3/subscription/{}".format(path_params['id']), headers=headers)

    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def obtain_report_for_subscription(path_params):
    validator.id_path_param(path_params)
    headers = {'x-api-key': API_KEY}
    conn.request("GET", "/v3/subscription/report/{}".format(path_params['id']), headers=headers)

    #   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))