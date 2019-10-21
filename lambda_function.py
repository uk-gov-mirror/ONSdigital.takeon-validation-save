from parse_validation import parse_validation_save_data
import json
import requests
import os


def lambda_handler(event, context):
    print('Event: ' + str(event))
    queue_data = event['Records'][0]['body']
    extracted_queue_data = queue_data.strip('\n')
    data_to_be_parsed = json.loads(extracted_queue_data)

    business_layer_endpoint = os.getenv("BUSINESS_LAYER_ENDPOINT")
    data_to_business_layer = parse_validation_save_data(data_to_be_parsed)

    try:
        request_response = requests.post(business_layer_endpoint, data_to_business_layer)
        print('Response: ' + str(request_response))
        print(request_response.text, "TEXT")
        print(request_response.content, "CONTENT")
        print(request_response.status_code, "STATUS CODE")
    except:
        request_response = ''
        print("{\"Error\": \"Problem with call to Business Layer\"}")
        print('Response: ' + str(request_response))
        print(request_response.content, "CONTENT")
        print(request_response.text, "TEXT")
        print(request_response.status_code, "STATUS CODE")
        return request_response.content
