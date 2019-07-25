# Author: CZ
# Time: 2019-07-25 7:35

import json
import base64
import requests

with open("1.png", "rb") as f:
    pic1 = f.read()

with open("2.png", "rb") as f:
    pic2 = f.read()

image_data = json.dumps(
    [
        {"image": str(base64.b64encode(pic1), "utf-8"), "image_type": "BASE64", "face_type": "LIVE",
         "quality_control": "LOW"},
        {"image": str(base64.b64encode(pic2), "utf-8"), "image_type": "BASE64", "face_type": "IDCARD",
         "quality_control": "LOW"},
    ]
)

get_token = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"
API_url = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="

text = requests.get(get_token).text
access_token = json.loads(text)['access_token']
url = API_url + access_token


response = requests.post(url, image_data)
print()
score = json.loads(response.text)['result']['score']
if score > 80:
    print("Image Similarity：%s  They are one person" % score)
else:
    print("Image Similarity：%s  They are not one person" % score)
