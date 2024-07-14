import sys
from pathlib import Path

import requests
import json

sys.path.append(str(Path(__file__).parent.parent))  # noqa
from utils.utils import (
    image_to_base64,
    base64_to_image
) # noqa


def face_gen(image_base64, key, prompt, negative_prompt):
    
    # print(image_base64)
    # convert image_base64 to image -> Get width and height
    image = base64_to_image(image_base64)
    width = str(image.shape[1])
    height = str(image.shape[0])
    print(width, height)
    
    url = "https://modelslab.com/api/v6/image_editing/head_shot"

    payload = json.dumps({
    "key": key,
    "prompt": "pretty woman",
    "negative_prompt": "anime, cartoon, drawing, big nose, long nose, fat, ugly, big lips, big mouth, face proportion mismatch, unrealistic, monochrome, lowres, bad anatomy, worst quality, low quality, blurry",
    "face_image":"https://media.allure.com/photos/647f876463cd1ef47aab9c88/3:2/w_2465,h_1643,c_limit/angelina%20jolie%20blonde%20hair%20chloe.jpg",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "21",
    "safety_checker": False,
    "base64": False,
    "seed": None,
    "guidance_scale": 7.5,
    "webhook": None,
    "track_id": None
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    
    out = json.loads(response.text)
    id = out['id']
    url = f"https://modelslab.com/api/v6/image_editing/fetch/{id}"

    payload = json.dumps({
    "key": key
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
        
    
