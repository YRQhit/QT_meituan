import requests
import json

import os
import base64
from PIL import Image

import base64
from PIL import Image
import io


def resize_image(image, max_size):
    width, height = image.size
    if max(width, height) > max_size:
        ratio = max_size / max(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        return image.resize((new_width, new_height))
    return image


def image_to_base64(image_path, max_size=4096):
    # Open image
    with open(image_path, 'rb') as img_file:
        img = Image.open(img_file)

        # Resize image if needed
        img = resize_image(img, max_size)

        # Convert image to base64
        img_base64 = base64.b64encode(img.convert("RGB").tobytes())
        # print(img_base64.decode('utf-8'))
        return img_base64.decode('utf-8')

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XXXXX&client_secret=XXXXXXX"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

def resize_image(image, max_size=4096, min_short_side=15):
    width, height = image.size
    if min(width, height) < min_short_side:
        ratio = min_short_side / min(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height))

    if max(width, height) > max_size:
        ratio = max_size / max(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height))

    return image


def image_to_base64(image_path, max_size=4096, min_short_side=15):
    # Open image
    with open(image_path, 'rb') as img_file:
        img = Image.open(img_file)

        # Resize image if needed
        img = resize_image(img, max_size, min_short_side)

        # Convert image to base64
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")  # 保存为JPEG格式，这样可以确保更好的压缩
        img_base64 = base64.b64encode(buffered.getvalue())

        return img_base64.decode('utf-8')


def resize_image(image, max_size=4096, min_short_side=15):
    width, height = image.size
    if min(width, height) < min_short_side:
        ratio = min_short_side / min(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height))

    if max(width, height) > max_size:
        ratio = max_size / max(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        image = image.resize((new_width, new_height))

    return image


def image_to_base64(image_path, max_size=4096, min_short_side=15):
    # Open image
    with open(image_path, 'rb') as img_file:
        img = Image.open(img_file)

        # Resize image if needed
        img = resize_image(img, max_size, min_short_side)

        # Convert image to base64
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")  # 保存为JPEG格式，这样可以确保更好的压缩
        img_base64 = base64.b64encode(buffered.getvalue())

        return img_base64.decode('utf-8')

def getAdvertisement(ID):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/image2text/fuyu_8b?access_token=" + get_access_token()
    image_path = "Picture/{}.jpg".format(ID)

    payload = json.dumps({
        "prompt": "给这个图片写一个广告",
        "image": image_to_base64(image_path)
    })
    headers = {
        'Content-Type': 'application/json'
    }
    # print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    # print(response)
    return json.loads(response.text)["result"]