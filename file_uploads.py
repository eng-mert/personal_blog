import os
import secrets
import requests


def save_image(image_field):
    from app import app
    app_root = app.root_path
    hex_name = secrets.token_hex(8)
    _, ext = os.path.splitext(image_field.filename)
    file_name = hex_name + ext
    save_path = os.path.join(app_root, 'app/static/uploads', file_name)
    image_field.save(save_path)
    return file_name


class GoFile:
    __token = 'NHRfBeCM2R62Wg0YEqQbrmgg97XBu1Ih'
    __base_url = 'https://api.gofile.io'
    __root_folder_id = '704d4dba-546a-4048-af5e-0a968ec82777'

    @classmethod
    def get_account_details(cls):
        response = requests.get(cls.__base_url + f'/getAccountDetails?token={cls.__token}&allDetails=true')
        return response.json()

    @classmethod
    def create_folder(cls, folder_name, parent_id=None):
        url = 'https://api.gofile.io/createFolder'
        data = {'parentFolderId': parent_id or cls.__root_folder_id, 'token': cls.__token,
                'folderName': folder_name}
        response = requests.put(url, data=data)
        return response.json()

    @classmethod
    def delete_content(cls, content_id):
        url = cls.__base_url + '/deleteFolder'
        data = {'contentId': content_id}
        response = requests.delete(url, data=data)
        return response.json()

    @classmethod
    def __get_server(cls):
        url = cls.__base_url + '/getServer'
        response = requests.get(url)
        return response.json().get('data').get('server')

    @classmethod
    def upload_file(cls, file_name, description='', folder_id=''):
        server = cls.__get_server()
        url = f'https://{server}.gofile.io/uploadFile'
        data = {'token': cls.__token, 'folderId': folder_id or cls.__root_folder_id}
        files = {(file_name, open(file_name, 'rb'))}
        response = requests.post(url, data=data, files=files)
        return response.json()

    @classmethod
    def delete_file(cls, content_id):
        url = 'https://api.gofile.io/deleteContent'
        data = {
            'contentId': content_id,
            'token': cls.__token
        }
        response = requests.delete(url, data=data)
        return response.json()
