import easyocr
import requests
import numpy as np
import cv2

# 全局只初始化一次
reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)  # 有GPU可以设为True，提高速度

def ocr_form_url_image(url):
    # 用requests下载图片
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # 用numpy数组识别
    result = reader.readtext(img)

    q = ""
    for detection in result:
        q = q + detection[1]  # detection[1] 是识别出来的文字

    return q
