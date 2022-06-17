# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\\tesseract.exe"
# image = Image.open("so5.png").convert("RGB")
# image_to_text = pytesseract.image_to_string(image,lang='eng')
# print(image_to_text)


# from google.cloud import vision
# import io,os
# def detect_text(path):
#     list_name = ""
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'key.json'
#     client = vision.ImageAnnotatorClient()
#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()
#     image = vision.Image(content=content)
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     for text in texts:
#     	list_name = text.description
#     	break
#     if response.error.message:
#         raise Exception(
#             '{}\nFor more info on error messages, check: '
#             'https://cloud.google.com/apis/design/errors'.format(
#                 response.error.message))
#     return list_name
# list_name = detect_text('so5.png')
# list_name = list_name.split("\n")
# for i in list_name:
# 	print(i)


# from PIL import Image
# im = Image.open("screen.png")
# im1 = im.crop((258, 121, 300, 143))
# im1.save("a.png")


# import pyautogui as pya
# from time import sleep as sl
# sl(2)
# for i in range(500):
# 	pya.click(x=555, y=902)



import requests

headers = {
	'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY1Mzk1NDczOSwiaWF0IjoxNjUzOTM2NzM5fQ.8Bh1kDynbAhf4ZaJDOL0E-nlhQVPbcUw4TIOmmuxBguv3uMOpEUFwx7ETdbjMu-_NCSv7UbrjYq_vhXlD8RvfQ'
}

url = "http://viuni.tk/user/update"

data = {
    "avatar_image": 1,
    "cover_image": 1,
    "current_city": 17,
    "hometown": 17
}

p = requests.put(url, headers = headers, json = data)
print(p.text)


# url = "http://viuni.tk/auth/login"

# data = {
#     "username": "admin",
#     "password": "12345678"
# }

# p = requests.post(url, json = data)
# print(p.text)