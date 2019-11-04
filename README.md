# takeon-validation-save

## About this repo
This repo is a lambda function that reads from 'TakeOn-Validation-SaveToDB' queue and then calls the business layer endpoint to save into 'validationoutput' table in the database.

## Environment Variables
EXECUTION_ROLE_ARN: The ARN of the Role with which the lambda will be executed. This role should have full access to SQS queue.
INPUT_QUEUE_URL: The URL of the Validation Save Queue (i.e of 'TakeOn-Validation-SaveToDB')
INPUT_QUEUE_ARN: The ARN of the Validation Save Queue (i.e of 'TakeOn-Validation-SaveToDB') 
BUSINESS_LAYER_ENDPOINT: The Business Layer's endpoint for validation save (e.g. validation/saveOutputs)
ERROR_QUEUE_URL: The URL of Validation Error Queue (i.e. of 'TakeOn-Validation-HandledErrors')

## Depolyment
This lambda deploymnet is implemented with serverless. 
'sls deploy --verbose' cammand can be used to deploy to aws. 
The serverless.yml file reads the values from 'config.dev.json' in the same directory. So variables like EXECUTION_ROLE_ARN, INPUT_QUEUE_URL, INPUT_QUEUE_ARN, BUSINESS_LAYER_ENDPOINT, ERROR_QUEUE_URL must be correctly set in 'config.dev.json' with corresponding values from AWS before deployment to AWS.  
Lambda Function name - takeon-validation-save-dev-main (It is generated from service name, stage and main function defined in serverless.yml)  
Lambda URL - https://eu-west-2.console.aws.amazon.com/lambda/home?region=eu-west-2#/functions/takeon-validation-save-dev-main?tab=configuration



## Sample Input JSON
The following JSON can be manually put in the input 'TakeOn-Validation-SaveToDB' queue to test this lambda    
```json
[ 
   { 
      "formula":"abs(20 - 0) > 20000 AND 20 > 0 AND 0 > 0",
      "metadata":{ 
         "validation":"POPM",
         "reference":"12345678001",
         "period":"201801",
         "survey":"999A",
         "validationid":21,
         "bpmid":"0"
      },
      "triggered":false
   },
   { 
      "formula":"20 != 0 AND ( 20 = 0 OR 0 = 0 ) AND abs(20 - 0) > 30000",
      "metadata":{ 
         "validation":"POPZC",
         "reference":"12345678001",
         "period":"201801",
         "survey":"999A",
         "validationid":41,
         "bpmid":"0"
      },
      "triggered":false
   },
   { 
      "formula":"20 != 21",
      "metadata":{ 
         "validation":"QVDQ",
         "reference":"12345678001",
         "period":"201801",
         "survey":"999A",
         "validationid":31,
         "bpmid":"0"
      },
      "triggered":true
   },
   { 
      "formula":"\"Rhubarb\" != \"\"",
      "metadata":{ 
         "validation":"VP",
         "reference":"12345678001",
         "period":"201801",
         "survey":"999A",
         "validationid":13,
         "bpmid":"0"
      },
      "triggered":true
   }
]
```
