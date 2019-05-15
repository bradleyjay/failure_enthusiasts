


# def generate_url(query_params):
#     return '<base_url_here>' + urllib.parse.urlencode(query_params)


# def make_request(url):
#     conn = http.client.HTTPSConnection("api.yelp.com")

#     conn.request('GET', url, headers=headers)

#     response = conn.getresponse()



# ----



import http.client
import urllib
import json
import time

def make_request():
    
    conn = http.client.HTTPSConnection("api.darksky.net")

    conn.request('GET','/forecast/c49ab0cc157f5ad35bdb1a9b0769853e/37.8267,-122.4233')

    response = conn.getresponse()

    return response


def decode_body_response(body):
    byte_body = body.read()
    string_body = byte_body.decode("utf-8")
    json_body = json.loads(string_body)

    return json_body

while True:

    result = make_request()
    final_result = decode_body_response(result)

    # print(final_result)


    print(final_result['currently']['temperature'])
    time.sleep(5)


