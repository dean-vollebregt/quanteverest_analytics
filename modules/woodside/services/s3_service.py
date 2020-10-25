import boto3

s3 = boto3.client('s3',  region_name='ap-southeast-2')

def upload_image():

    try:
        s3.upload_file(
            Filename="./images/brent_forecast.png",
            Bucket="www.quanteverest-dev.com",
            Key="images/brent_forecast.png")
    except Exception as e:
        print('Error uploading to S3: ', e)