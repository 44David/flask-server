from dotenv import load_dotenv
import os
import boto3, botocore
import io
from PIL import Image


class Upload():
    def s3_upload(self, buffer, img_name, img_type):
        # loads .env variables
        load_dotenv()

        bucket_name = os.environ['BUCKET_NAME']
        access_key = os.environ['ACCESS_KEY']
        access_secret = os.environ['SECRET_ACCESS_KEY']
        region = os.environ['BUCKET_REGION']
        s3_link = 'http://{}.s3.amazonaws.com/'.format(bucket_name)



        s3_client = boto3.client(
            "s3", 
            region_name=region,
            aws_access_key_id=access_key,
            aws_secret_access_key=access_secret
        )

        try:
                
            s3_client.upload_fileobj(
                buffer, 
                bucket_name, 
                img_name, 
                ExtraArgs={
                    "ContentType": img_type,
                }
            )
        except Exception as err:
            print("Error occurred", err)
            return err

        return "{}{}".format(s3_link, img_name)
