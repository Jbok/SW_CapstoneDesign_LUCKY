import json
import os
import base64

import boto3
from PIL import Image

import facial_landmark

s3_client = boto3.client('s3')

def respond(err, res):
    return {
        'statusCode': '400' if err else '200',
        'body': res,
        'headers': {
            'Content-Type': 'image/png',
        },
        'isBase64Encoded': 'true'
    }

def hello(event, context):


    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
        
        
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def downloadTrainedData(bucketName, trainedDataPath, localFilePath):
    s3_client.download_file(bucketName, trainedDataPath, localFilePath)


def imagetest(event, context):
    
    
    img_data = json.dumps(event['body'])

    BUCKET_NAME = 'lucky-faceweb-2019'
    BUCKET_TRAINED_DATA_PATH = 'TrainedData/shape_predictor_68_face_landmarks.dat'
    LOCAL_IMG_PATH = '/tmp/image.png'
    LOCAL_TRAINED_DATA_PATH = '/tmp/train.dat'

    fh = open(LOCAL_IMG_PATH, "wb")
    fh.write(img_data.decode('base64'))
    fh.close()

    # fh_temp = open(LOCAL_FILE_PATH, "r")
    # base64.encodestring(fh_temp.read())
    
    # s3_client.upload_file(FILE_NAME, BUCKET_NAME, 'imageToSave.png')

    downloadTrainedData(BUCKET_NAME, BUCKET_TRAINED_DATA_PATH, LOCAL_TRAINED_DATA_PATH)
    
    result = facial_landmark.faceLandmarks(LOCAL_TRAINED_DATA_PATH, LOCAL_IMG_PATH)

    response = {
        "statusCode": 200,
        # "message": "message",
        # "ssibal": "ssibal",
        "body": img_data
    }

    return response

def packagetest(event, context):

    response = {
        "statusCode": 200,
        "body": "Hello"
    }

    return response

