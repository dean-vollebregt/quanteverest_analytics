import boto3

s3 = boto3.client('s3',  region_name='ap-southeast-2')

def upload_image():

    try:
        s3.upload_file(
            Filename="./test.txt",
            Bucket="www.quanteverest-dev.com",
            Key="images/test.txt")
    except Exception as e:
        print("There has been an error in uploading the image to S3")

upload_image()