import json
import os
import base64

import boto3
from PIL import Image

import cv2
import numpy
import dlib

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

def downloadTrainedData():
    BUCKET_NAME = 'lucky-faceweb-2019'
    FILE_PATH = 'TrainedData/shape_predictor_68_face_landmarks.dat'
    LOCAL_FILE_PATH = 'train.dat'
    
    s3_client.download_file(BUCKET_NAME, FILE_PATH, LOCAL_FILE_PATH)


def imagetest(event, context):
    
    img_data = json.dumps(event['body'])

    fh = open("/tmp/imageToSave2.png", "wb")
    fh.write(img_data.decode('base64'))
    fh.close()

    fh_temp = open("/tmp/imageToSave2.png", "r")
    encode_temp = base64.encodestring(fh_temp.read())

    BUCKET_NAME = 'lucky-faceweb-2019'
    FILE_NAME = '/tmp/imageToSave2.png'

    s3_client.upload_file(FILE_NAME, BUCKET_NAME, 'imageToSave.png')


    response = {
        "statusCode": 200,
        # "message": img_data,
        "body": encode_temp + "\n\n\n\n" + img_data
        
        
    }

    return response

def packagetest(event, context):
    
    print(cv2.__version__)
    print(numpy.version.version)



    response = {
        "statusCode": 200,
        "body": cv2.__version__
    }

    return response


    