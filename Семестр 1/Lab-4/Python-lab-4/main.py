from tkinter import *

import pygame

from KeyBilder import buildkey

window = Tk()
window.title("Crazy hacking programm")
window.geometry("1280x791")
window.resizable(width=False, height=False)
im = PhotoImage(file='1.gif')
lab = Label(window, image=im)
lab.pack()
x = str(buildkey())
flag = 0
pygame.mixer.init()
pygame.mixer.music.load('05. BFG Division 2020.mp3')
pygame.mixer.music.play(-1)


def printing():
    global x
    label.config(text=x)


def check_sound():
    global flag
    if flag == 0:
        pygame.mixer.music.pause()
        flag += 1
    else:
        pygame.mixer.music.unpause()
        flag = 0


sound_b = Button(text="Sound off/on", command=check_sound)
sound_b.place(relx=0, rely=0, anchor="nw")
butt = Button(text="Click on the button to generate the key", command=printing)
butt.place(relx=0.5, rely=0.8, anchor="center")
label = Label(window, text="")
label.place(relx=0.5, rely=0.9, anchor="center")
window.mainloop()
