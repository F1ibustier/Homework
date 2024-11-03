# Обзор сторонних библиотек Python
# coded by f1ibustier
""" Библиотека Python Imaging Library (PIL) добавляет возможности обработки изображений в интерпретатор Python.
    Библиотека PIL идеально подходит для хранения изображений и пакетной обработки. Можно использовать библиотеку
для создания миниатюр, преобразования между форматами файлов, печати изображений и т. д.
    Библиотека содержит базовые функциональные возможности обработки изображений, включая операции с точками,
фильтрацию с помощью набора встроенных ядер свертки и преобразования цветового пространства.
    Библиотека также поддерживает изменение размера изображений, поворот и произвольные преобразования."""
from PIL import Image, ImageFont, ImageDraw
import requests

url = 'https://example.com/image.jpg'
response = requests.get(url)
with open('image.jpg', 'wb') as f:
    f.write(response.content)

with Image.open('ocean.jpg') as im:
    # Изменяю размер картинки и сохраняю ее под другим именем и в другом формате
    im = im.resize((im.width // 10, im.height // 10))
    im.save('resize_ocean.png')
    # Добавляю текст на картинку
    font = ImageFont.truetype('С:/Windows/lucon.ttf', size=18)
    draw_text = ImageDraw.Draw(im)
    draw_text.text((100, 100), 'Картинка стала меньше', font=font, fill='#1C0606')
    im.show()
