from microbit import *
import random
FirstName= ["Steve","Shannon","Jenny"]
SecondName= ["Debank","Green","Penny","Smith"]
while True:
  display.scroll(random.choice(FirstName))
  sleep(1000)
  display.scroll(random.choice(SecondName))
  sleep(1000)
