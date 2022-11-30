from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
def diode():
 B = nothing
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, O, B, O, O, O, B, O,
 O, O, B, B, O, O, B, O,
 O, O, B, B, B, O, B, O,
 B, B, B, B, B, B, B, B,
 O, O, B, B, B, O, B, O,
 O, O, B, B, O, O, B, O,
 O, O, B, O, O, O, B, O
 ]
 return logo
def S():
 B = blue
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, O, B, B, B, B, O, O,
 O, O, B, O, O, O, O, O,
 O, O, B, O, O, O, O, O,
 O, O, B, B, B, B, O, O,
 O, O, O, O, O, B, O, O,
 O, O, O, O, O, B, O, O,
 O, O, B, B, B, B, O, O
 ]
 return logo
def R():
  B = blue
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, O, B, B, B, B, O, O,
 O, O, B, O, O, B, O, O,
 O, O, B, O, O, B, O, O,
 O, O, B, B, B, B, O, O,
 O, O, B, B, O, O, O, O,
 O, O, B, O, B, O, O, O,
 O, O, B, O, O, B, O, O
 ]
 return logo

def M():
 B = blue
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, O, B, O, O, O, B, O,
 O, O, B, B, O, B, B, O,
 O, O, B, O, B, O, B, O,
 O, O, B, O, O, O, B, O,
 O, O, B, O, O, O, B, O,
 O, O, B, O, O, O, B, O,
 O, O, B, O, O, O, B, O
 ]
 return logo
def blank():
 B = blue
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O
 ]
 return logo

def I():
 B = blue O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, B, B, B, B, B, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, B, B, B, B, B, O, O
 ]
 return logo
def T():
 B = blue
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, B, B, B, B, B, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O,
 O, O, O, B, O, O, O, O
 ]
 return logo

def give_way():
 R = red
 O = white
 logo = [
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O,
 R, R, R, R, R, R, R, R,
 O, R, O, O, O, O, R, O,
 O, O, R, O, O, R, O, O,
 O, O, O, R, R, O, O, O,
 O, O, O, O, O, O, O, O,
 O, O, O, O, O, O, O, O
 ]
 return logo

lis = [S, R, M, blank, I, S, T, blank, diode, blank, give_way]
count = 0 while True:
 s.set_pixels(lis[count % len(lis)]())
 time.sleep(.75)
 count += 1
