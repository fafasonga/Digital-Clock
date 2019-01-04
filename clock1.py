#!/usr/bin/env python3
# -*- coding: cp1252 -*-

from turtle import *
from time import strftime
from datetime import datetime

mode("logo")

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(- laenge * 0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)


def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 145, 0)
    make_hand_shape("minute_hand",  130, 15)
    make_hand_shape("hour_hand", 50, 15)
    clockface(170)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("chocolate", "NavajoWhite")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "red1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("black", "red3")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    # writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)


def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s / %d / %d" % (m, t, j)

def digital(d):
    while True:
        return strftime("%m/%d/%Y %H:%M:%S")

def tick():
    t = datetime.today()
    n = datetime.now()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    tracer(False)
    writer.clear()
    writer.home()
    writer.forward(100)
    writer.write(wochentag(t),
                 align="center", font=("Courier", 26, "bold"))
    writer.back(180)
    writer.write(datum(t),
                 align="center", font=("Courier", 14, "bold"))
    writer.back(20)
    writer.write(digital(n),
                 align="center", font=("Courier", 18, "bold"))
    writer.backward(170)
    tracer(True)
    second_hand.setheading(6 * sekunde)
    minute_hand.setheading(6 * minute)
    hour_hand.setheading(30 * stunde)
    tracer(True)
    ontimer(tick, 100)


def main():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "Clock Started"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

