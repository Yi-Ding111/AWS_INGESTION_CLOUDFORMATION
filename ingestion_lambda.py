import requests 
import boto3
import json

s3=boto3.client('s3')

#weatherstack API
api_key=''
endpoint = 'http://api.weatherstack.com/current'

params = {
        'access_key': api_key,
        'query': 'Sydney'
        }

def lambda_handler(event, context):
    #get today's weather info
    api_result = requests.get(endpoint, params)
    api_response = api_result.json()

    #reconstruct data
    payload={
        'city':api_response["location"]["name"],
        'country':api_response["location"]["country"],
        'ingest_time':api_response["location"]["localtime"],
        'observation_time':api_response["current"]["observation_time"],
        'temperature':api_response["current"]["temperature"],
        'weather_descriptions':api_response["current"]["weather_descriptions"],
        'wind_speed':api_response["current"]["wind_speed"],
        'wind_degree':api_response["current"]["wind_degree"],
        'wind_dir':api_response["current"]["wind_dir"],
        'cloudcover':api_response["current"]["cloudcover"]
    }
    
    #load data into s3 bucket
    data=json.dumps(payload)
    filename=api_response["location"]["localtime"]+".json"
    
    s3.put_object(Bucket="<! DESTINATION_BUCKET_NANE >",Key=filename,Body=data)
