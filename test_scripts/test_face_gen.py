import sys 
from pathlib import Path
from dotenv import load_dotenv

import requests
import json
import cv2
import os

sys.path.append(str(Path(__file__).parent.parent))  # noqa
from utils.utils import (
    image_to_base64,
    base64_to_image
    )
from face_gen.facegen import face_gen

ad_api_key = os.environ['SD_API_KEY']
print(ad_api_key)

image = cv2.imread("data/test/DngBack.jpeg")
image_base64 = image_to_base64(image)
# print(image_base64)
response = face_gen(image_base64, ad_api_key, "A guy in the beach", "blur")
print(response)
