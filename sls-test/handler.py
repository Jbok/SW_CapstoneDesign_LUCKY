import json

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import math

# python AWS SDK
import boto3
import urllib
from PIL import Image
import PIL.Image

def temp(event, contet):
    BUCKET_NAME = 'lucky-faceweb-2019'
    FILE_NAME = 'test_image.png'
    s3 = boto3.resource('s3', region_name='ap-northeast-2')
    
    s3.Bucket(BUCKET_NAME).download_file(FILE_NAME, 'test_image.png')
    img = cv2.imread('test_image.png')
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def open_image(image_path, resized_path):
    with Image.open(image_path) as image:
        cv2.imshow(image)
        
def handler(event, contet):
    BUCKET_NAME = 'sls-test-dev-serverlessdeploymentbucket-gfkswqtg50dd'
    FILE_NAME = 'shape_predictor_68_face_landmarks.dat'
    s3_resource = boto3.resource('s3')
    s3_resource.Bucket(BUCKET_NAME).download_file(FILE_NAME, 'temp1.dat')

    



"""
client = boto3.client('s3')
resource = boto3.re


MODEL_FILE_NAME = 'shape_predictor_68_face_landmarks.dat'
MODEL_LOCAL_PATH = '/tmp/' + MODEL_FILE_NAME

def load_model():
    conn = S3Connection()
    bucket = conn.create_bucket(BUCKET_NAME)
    key_obj = Key(bucket)
    key_obj.key = MODEL_FILE_NAME

    contents = key_obj.get_contents_to_filename(MODEL_LOCAL_PATH)
    return joblib.load(MODEL_LOCAL_PATH)
"""





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

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def main(event, context):

    s3_client = boto3.client('s3')

    print("Your numpy array:")
    
    print(cv2.__version__)
	
    print("FUCCCCCCCK")

    bucketname = 'sls-test-dev-serverlessdeploymentbucket-gfkswqtg50dd'
    filename = 's3.png'
    
    opener = urllib.URLopener()
    myurl = 'https://s3.amazonaws.com/sls-test-dev-serverlessdeploymentbucket-gfkswqtg50dd/temp.txt'

    myfile = opener.open(myurl)


    
    


    





if __name__ == "__main__":
    main('', '')
