from parse_validation import parse_validation_save_data
import json
import requests


business_layer_endpoint = '/contributor/validationOutputSave'
business_layer_endpoint_local = 'http://192.168.99.113:31303/contributor/validationOutputSave'

def lambda_handler(event, context):
    print('Event: ' + str(event))
    queue_data = event['Records'][0]['body']
    extracted_queue_data = queue_data.strip('\n')
    data_to_be_parsed = json.loads(extracted_queue_data)

    data_to_business_layer = parse_validation_save_data(data_to_be_parsed)

    try:
        request_response = requests.post(business_layer_endpoint, data_to_business_layer)
        print('Response: ' + str(request_response))
        print(request_response.text, "TEXT")
        print(request_response.content, "CONTENT")
        print(request_response.status_code, "STATUS CODE")
    except:
        print("{\"Error\": \"Problem with call to Business Layer\"}")
        print('Response: ' + str(request_response))
        print(request_response.content, "CONTENT")
        print(request_response.text, "TEXT")
        print(request_response.status_code, "STATUS CODE")
        return(request_response.content)
