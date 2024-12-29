from dotenv import load_dotenv
import os
import boto3, botocore

def upload():
    # loads .env variables
    load_dotenv()

    # Figure out how to access file
    # file = 

    bucket_name = os.environ['BUCKET_NAME']
    access_key = os.environ['ACCESS_KEY']
    access_secret = os.environ['SECRET_ACCESS_KEY']
    region = os.environ['BUCKET_REGION']
    s3_link = 'http://{}.s3.amazonaws.com/'.format(bucket_name)

    s3_client = boto3.client(
        "s3", 
        access_key,
        access_secret
    )

    try:
            
        s3_client.upload_fileobj(
            file, 
            bucket_name, 
            file.filename, 
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": file.content_type,
            }
        )
    except Exception as err:
        print("Error occurred", err)
        return err

    return "{}{}".format(s3_link, file.filename)


upload()