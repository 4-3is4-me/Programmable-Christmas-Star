from star2 import star2
from time import sleep

mystar = star2(speed = 0.15)

# all is the whole star
# centre is the centre star
# inp is the inner pairs of LEDS on each arm
# outp is the outer pairs of LEDS on each arm
# tips is the tips of each arm
# first is the top arm, second is the next arm clockwise, third is next and so on through fourth and fith

speed = 0.15

for i in range(5):
    mystar.on(mystar.all)
    sleep(speed)
    mystar.off(mystar.centre)
    sleep(speed)
    mystar.off(mystar.all)
    sleep(speed)
    mystar.on(mystar.centre)
    sleep(speed)
    mystar.on(mystar.all)
    sleep(speed)

mystar.rippleoff(5)
mystar.rippleoffrev(5)
mystar.rippleon(5)
mystar.rippleonrev(5)
mystar.clockonfill(5)
mystar.clockofffill(5)
mystar.clockflashoff(5)
mystar.anticlockflashoff(5)
mystar.grow(5)
mystar.shrink(5)
mystar.growoff(5)
mystar.shrinkon(5)
