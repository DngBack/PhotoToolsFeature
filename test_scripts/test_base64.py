import cv2
import base64
import numpy as np

def image_to_base64(image):
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    return image_base64

def base64_to_image(image_base64):
    image_data = base64.b64decode(image_base64)
    np_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    return image

def main():
    # Đường dẫn tới ảnh của bạn
    image_path = 'data/test/DngBack.jpeg'
    # Đường dẫn để lưu ảnh kết quả
    output_image_path = 'data/output/DngBack.png'

    # Đọc ảnh từ file
    image = cv2.imread(image_path)

    if image is None:
        print(f"Failed to load image at {image_path}")
        return

    # Chuyển ảnh sang base64
    image_base64 = image_to_base64(image)
    print("Image in base64:", image_base64[:100], "...")  # In 100 ký tự đầu tiên để xem

    # Chuyển base64 ngược lại thành ảnh
    image_decoded = base64_to_image(image_base64)

    # Lưu ảnh kết quả ở định dạng PNG
    cv2.imwrite(output_image_path, image_decoded)
    print(f"Decoded image saved to {output_image_path}")

if __name__ == "__main__":
    main()
