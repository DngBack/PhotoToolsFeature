import cv2
import base64
import numpy as np

def image_to_base64(image):
    # Chuyển đổi ảnh từ định dạng BGR (mặc định của OpenCV) sang định dạng JPEG
    _, buffer = cv2.imencode('.jpg', image)
    # Mã hóa ảnh thành chuỗi base64
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    return image_base64

def base64_to_image(image_base64):
    # Giải mã chuỗi base64 thành byte buffer
    image_data = base64.b64decode(image_base64)
    # Chuyển đổi byte buffer thành numpy array
    np_array = np.frombuffer(image_data, np.uint8)
    # Giải mã numpy array thành ảnh OpenCV
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return image
