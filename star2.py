from time import sleep
from gpiozero import LEDBoard

# reference: position and bcm pin number - 0 is top and going clockwise:
# 0-8, 1-7, 2-12, 3-21, 4-20, 5-16, 6-26, 7-19, 8-13, 9-6, 10-5, 11-11,
# 12-9, 13-10, 14-22, 15-27, 16-17, 17-4, 18-3, 19-14, 20-23, 21-18,
# 22-15, 23-24, 24-25, 25-2

# position 25 (gpio 2) is centre

class star2:
    def __init__(self, speed):
        self.star2 = LEDBoard(8, 7, 12, 21, 20, 16, 26, 19, 13, 6, 5, 11, 9,
                10, 22, 27, 17, 4, 3, 14, 23, 18, 15, 24, 25, 2,
                initial_value=False, pwm=False)


        self.alli = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        self.all = [self.star2[i] for i in self.alli] # makes a list of all star2[] objects
        # list of indices in star for outerpairs
        self.outpairs = [24, 1, 4, 6, 9, 11, 14, 16, 19, 21]
        self.outp = [self.star2[i] for i in self.outpairs] # makes a list of star2[] objects for outerpairs
        # list of indices in star for innerpairs
        self.inpairs = [23, 2, 3, 7, 8, 12, 13, 17, 18, 22]
        self.inp = [self.star2[i] for i in self.inpairs]
        # list of indices in star for tips
        self.tipsies = [0, 5, 10, 15, 20]
        self.tips = [self.star2[i] for i in self.tipsies]
        # the centre star
        self.centrei = [25]
        self.centre = [self.star2[i] for i in self.centrei]

        # the arms of the star clockwise
        self.firsti = [0,1,2,23,24]
        self.first = [self.star2[i] for i in self.firsti]
        self.secondi = [3,4,5,6,7]
        self.second = [self.star2[i] for i in self.secondi]
        self.thirdi = [8,9,10,11,12]
        self.third = [self.star2[i] for i in self.thirdi]
        self.fourthi = [13,14,15,16,17]
        self.fourth = [self.star2[i] for i in self.fourthi]
        self.fithi = [18,19,20,21,22]
        self.fith = [self.star2[i] for i in self.fithi]

        self.speed = speed   # I like 0.15

    def on(self, ref):
        for i in ref:
            i.on()

    def off(self, ref):
        for i in ref:
            i.off()

    def flashoff(self, ref, delay):
        self.off(ref)
        sleep(delay)
        self.on(ref)

    def flashon(self, ref, delay):
        self.on(ref)
        sleep(delay)
        self.off(ref)

################################################################

    def rippleoff(self, repeats):
        self.star2.on()
        order = [self.centre, self.inp, self.outp, self.tips]
        for r in range(repeats):
            for o in order:
                self.flashoff(o, self.speed)
            sleep(self.speed)

    def rippleoffrev(self, repeats):
        self.star2.on()
        order = [self.tips, self.outp, self.inp, self.centre]
        for r in range(repeats):
            for o in order:
                self.flashoff(o, self.speed)
            sleep(self.speed)

    def rippleon(self, repeats):
        self.star2.off()
        order = [self.centre, self.inp, self.outp, self.tips]
        for r in range(repeats):
            for o in order:
                self.flashon(o, self.speed)
            sleep(self.speed)

    def rippleonrev(self, repeats):
        self.star2.off()
        order = [self.tips, self.outp, self.inp, self.centre]
        for r in range(repeats):
            for o in order:
                self.flashon(o, self.speed)
            sleep(self.speed)

    def clockonfill(self, repeats):
        self.star2.off()
        order = [self.first, self.second, self.third, self.fourth, self.fith]
        for r in range(repeats):
            self.star2.off()
            sleep(self.speed)
            for o in order:
                self.on(o)
                sleep(self.speed)

    def clockofffill(self, repeats):
        self.star2.on()
        order = [self.first, self.second, self.third, self.fourth, self.fith]
        for r in range(repeats):
            self.star2.on()
            sleep(self.speed)
            for o in order:
                self.off(o)
                sleep(self.speed)

    def clockflashoff(self, repeats):
        self.star2.on()
        order = [self.first, self.second, self.third, self.fourth, self.fith]
        for r in range(repeats):
            for o in order:
                self.flashoff(o, self.speed)
            sleep(self.speed)

    def anticlockflashoff(self, repeats):
        self.star2.on()
        order = [self.first, self.fith, self.fourth, self.third, self.second]
        for r in range(repeats):
            for o in order:
                self.flashoff(o, self.speed)
            sleep(self.speed)

    def grow(self, repeats):
        self.star2.off()
        order = [self.centre, self.inp, self.outp, self.tips]
        for r in range(repeats):
            self.star2.off()
            sleep(self.speed)
            for o in order:
                self.on(o)
                sleep(self.speed)

    def growoff(self, repeats):
        self.star2.on()
        order = [self.centre, self.inp, self.outp, self.tips]
        for r in range(repeats):
            self.star2.on()
            sleep(self.speed)
            for o in order:
                self.off(o)
                sleep(self.speed)

    def shrink(self, repeats):
        self.star2.on()
        order = [self.tips, self.outp, self.inp, self.centre]
        for r in range(repeats):
            self.star2.on()
            sleep(self.speed)
            for o in order:
                self.off(o)
                sleep(self.speed)

    def shrinkon(self, repeats):
        self.star2.off()
        order = [self.tips, self.outp, self.inp, self.centre]
        for r in range(repeats):
            self.star2.off()
            sleep(self.speed)
            for o in order:
                self.on(o)
                sleep(self.speed)
