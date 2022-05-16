#!/usr/bin/python3

from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

morseTable = {"A": ".-",     "B": "-...",   "C": "-.-.",
        "D": "-..",    "E": ".",      "F": "..-.",
        "G": "--.",    "H": "....",   "I": "..",
        "J": ".---",   "K": "-.-",    "L": ".-..",
        "M": "--",     "N": "-.",     "O": "---",
        "P": ".--.",   "Q": "--.-",   "R": ".-.",
        "S": "...",    "T": "-",      "U": "..-",
        "V": "...-",   "W": ".--",    "X": "-..-",
        "Y": "-.--",   "Z": "--..",

        "0": "-----",  "1": ".----",  "2": "..---",
        "3": "...--",  "4": "....-",  "5": ".....",
        "6": "-....",  "7": "--...",  "8": "---..",
        "9": "----."
        }

def textToMorse():
    morseString = []
    text = txt.get()
    text = text.upper()
    for letter in text:
        for i, j in iter(morseTable.items()):
            if letter == i:
                morseString.append(j)
    morseString = ("".join(morseString))
    morseString = list(morseString)
    ledMorse(morseString)

def ledMorse(separated):
    for sym in separated:
        if sym == '.':
            GPIO.output(14, GPIO.HIGH )
            time.sleep(0.1)
            GPIO.output(14, GPIO.LOW )
            time.sleep(0.1)
        elif sym == '-':
            GPIO.output(14, GPIO.HIGH )
            time.sleep(0.3)
            GPIO.output(14, GPIO.LOW )
            time.sleep(0.3)

def callback(sv):
    c = sv.get()[0:12]
    print("c=", c)
    sv.set(c)

window = Tk()

sv = StringVar()

sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

txt = Entry(window,width=12, textvariable=sv)

txt.grid(column=1, row=0)

btn = Button(window, text="Execute Morse Code", command=textToMorse)

btn.grid(column=2, row=0)

window.title("Morse code LED")

window.geometry('350x200')

window.mainloop()
