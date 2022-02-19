import os
import secrets


def save_image(image_field):
    from app import app
    app_root = app.root_path
    hex_name = secrets.token_hex(8)
    _, ext = os.path.splitext(image_field.filename)
    file_name = hex_name + ext
    save_path = os.path.join(app_root, 'static/uploads', file_name)
    image_field.save(save_path)
    return file_name
