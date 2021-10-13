name = input("enter your name :")
date = input("enter todays date :")
import time
delay=60*1
t_end = time.time() + delay
while True:

    water=1
    print("drink Water")
    z=input()
    if z=="yes":
        water+=1
    else:
        water+=0

    if time.time() > t_end:
        break
if water>=7:
    print("Good Job Your Hydrated")
else:
    print("You should Drink More water")
