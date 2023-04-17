import os
from tkinter import *

import requests
from PIL import ImageTk, Image
from bs4 import BeautifulSoup


def get_image():
    url = 'https://apod.nasa.gov/apod/astropix.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find('img')
    img_url = 'https://apod.nasa.gov/apod/' + img_tag['src']
    img_response = requests.get(img_url)
    img_name = os.path.basename(img_url)
    with open(img_name, 'wb') as f:
        f.write(img_response.content)
    return img_name


window = Tk()
window.title("NASA photo a day")
canvas = Canvas(window, width=800, height=600)
canvas.pack()

img_name = get_image()
img = Image.open(img_name)
img = img.resize((800, 600), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

canvas.create_image(0, 0, anchor=NW, image=photo)

window.mainloop()
