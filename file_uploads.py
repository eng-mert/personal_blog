import os
import secrets
import boto3
from config import Config


# def save_image(image_field):
#     from app import app
#     app_root = app.root_path
#     hex_name = secrets.token_hex(8)
#     _, ext = os.path.splitext(image_field.filename)
#     file_name = hex_name + ext
#     save_path = os.path.join(app_root, 'app/static/uploads', file_name)
#     image_field.save(save_path)
#     return file_name


def upload_image_to_s3(image_field,acl = "public-read"):
    s3 = boto3.client(
        's3',
        aws_access_key_id=Config.ACCESS_KEY_ID,
        aws_secret_access_key=Config.ACCESS_SECRET_KEY
    )
    try:
        hex_text = secrets.token_hex(8)
        _, ext = os.path.splitext(image_field.filename)
        hex_name = hex_text + ext
        #filename = image_field.filename
        s3.upload_fileobj(image_field, Config.S3_BUCKET_NAME,
                          hex_name,
                          ExtraArgs={"ACL": acl, "ContentType": image_field.content_type})
        print('Uploaded Done')
        return Config.S3_LOCATION + hex_name

    except Exception as e:
        print(e)

