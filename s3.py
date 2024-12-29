from dotenv import load_dotenv
import os
import boto3, botocore

def upload():
    # loads .env variables
    load_dotenv()

    # Figoure out how to access file
    # file = 

    bucket_name = os.environ['S3_BUCKET']
    access_key = os.environ['S3_ACCESS_KEY']
    access_secret = os.environ['S3_ACCESS_SECRET']
    region = os.environ['S3_REGION']
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