from __fututre__ import print_function
import RPi.GPIO as GPIO
import time
import pygame
import random

class Experiment():

    def __init__(self, startdate):
        self.feeder = 26
        self.pastR = []
        self.good = True
        self.startT = 42;
        self.duration = 1
        self.stopT = self.startT + self.duration
        #self.startCamera = 35
        #self.filmT = 15
        #self.stopCamera = self.startCamera + self.filmT
        self.startAcclim = startdate
        self.acclimT = 3
        self.startTrain = self.startAcclim + self.acclimT
        self.proposedR = random.randint(1 , 2)
        self.acclimTimes = [9, 16]
        self.trainTimes = [8, 11, 14, 17]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.feeder, GPIO.OUT)
        GPIO.output(self.feeder, True)
        self.pygameSetup()

    def pygameSetup(self):
        self.screenSize = pygame.display.Info()
        self.screen = pygame.display.set_mode((self.screenSize.current_w, self.screenSize.current_h))
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.vertBarW = int(self.screenSize.current_w()/10)
        self.horizBarH = int(self.screenSize.current_h()/7)
        self.run = True
    
    def feeder(self, feed):
        if feed == True:
            GPIO.output(self.feeder, False)
            # turn feeder off ???
        else:
            GPIO.output(self.feeder, True)

    def update_orientation(self):
        self.proposedR = random.randint(1 , 2)
        self.good = False
        if len(self.pastR)<3:
            self.good = True
        while not self.good:
            self.self.proposedR = random.randint(1 , 2)
            if self.proposedR==self.pastR[-1] and self.proposedR==self.pastR[-2] and self.proposedR==self.pastR[-3]:
                self.good = False
            else:
                self.good = True



    def draw(self, orientation):
        self.screen.fill(white)
        if orientation == 1:
            # 10 vertical lines
            for i in range(0, 9):
                pygame.draw.rect(self.screen, self.black, (2*i, 0, self.vertBarW, int(self.screenSize.current_h())))
        if orientation == 2:
            # 8 horizontal lines
            for i in range(0, 7):
                pygame.draw.rect(self.screen, self.black, (0, 2*i, int(self.screenSize.current_h()), self.horizBarW))

    def main(self):
        while self.run == True:
            if time.loacaltime().tm_yday<startTrain:
                if int(if int(time.localtime().tm_hr) in self.acclimTimes:
                    if int(time.localtime().tm_min)==36 and int(time.localtime().tm_sec)>=0:
                        feeder(True)
                    if int(time.localtime().tm_min)==36 and int(time.localtime().tm_sec)>30:
                        feeder(False)

            if time.localtime().tm_yday>=startTrain:
                if int(time.localtime().tm_hr) in self.trainTimes:


        # record Rs             
        record = open('/home/pi/rlog.txt', 'a')
        record.write(self.proposedR + '\n')
        record.close()


if __name__ == '__main__':
    
    x = Experiment(time.localtime().tm_yday
    x.main()

