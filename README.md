## WEATHER API INGESTION
---

### On AWS services: S3, EventBridge Rule, Lambda, IAM Role, CloudFormation

* API source: from https://weatherstack.com/ . 

    The API endpoint chooses from Current Weather: Get current weather data.

* This project will extract weather data using AWS Lambda on schedule at a regular rate (each 12 hours), and load data into corresponding S3 Bucket. The following is all steps to set up the process.
    
    1. Lambda function needs REQUESTS package as a layer. Load [python.zip](python.zip) into one existing S3 Bucket.

    2. Run [Cloudformation.yaml](Cloudformation.yaml) to set up all AWS configrations.

    3. Give Cloudformation Template Parameters:
        
        * LambdaFunctionName: Give the Lambda a name (default)
        * LambdaRole: Give the Lambda Execution Role (IAM Role) a name (default)
        * LayerVersionBucket: Give the Bucket a name where the Lambda layer zip stored
        * EventBridgeSchedule: Give the event rule a name (default)
        * S3BucketName: Give the S3 Bucket a name
    
    4. MENTION: Users need to change DESTINATION BUCKET NAME in the Lambda function.


---
Creator: YI DING

