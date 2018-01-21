from microbit import *
display.scroll("More useful For loop")
Names_List=["Steve","Alex","Adam"]
for i in range(len(Names_List)):
  display.scroll(Names_List[i])
  sleep(300)
