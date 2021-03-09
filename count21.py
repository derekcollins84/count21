import RPi.GPIO as GPIO
import random
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.setup(25,GPIO.OUT)

GPIO.setup(16,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(21,GPIO.IN)

cardsInDeck = 52
runningCount = 0
trueCount = 0

def main():
  global cardsInDeck

  while cardsInDeck > 1:
    time.sleep(.2)
    currentCard = inputCard()
    if trueCount >= 2:
      GPIO.output(17,GPIO.HIGH)
      GPIO.output(27,GPIO.LOW)
      GPIO.output(22,GPIO.LOW)
    elif trueCount < 2 and trueCount > .55:
      GPIO.output(17,GPIO.LOW)
      GPIO.output(27,GPIO.HIGH)
      GPIO.output(22,GPIO.LOW)
    elif trueCount <= .55:
      GPIO.output(17,GPIO.LOW)
      GPIO.output(27,GPIO.LOW)
      GPIO.output(22,GPIO.HIGH)

def inputCard():
  global cardsInDeck
  global runningCount
  global trueCount

  GPIO.output(25,GPIO.HIGH)

  if GPIO.input(21):
    runningCount = runningCount + 1
    trueCount = runningCount / (cardsInDeck / 52)
    cardsInDeck = cardsInDeck - 1
    GPIO.output(25,GPIO.LOW)
    print('low ',runningCount, trueCount)
    time.sleep(1)

  if GPIO.input(16):
    trueCount = runningCount / (cardsInDeck / 52)
    cardsInDeck - cardsInDeck - 1
    GPIO.output(25,GPIO.LOW)
    print('neutral ',runningCount, trueCount)
    time.sleep(1)

  if GPIO.input(12):
    runningCount = runningCount - 1
    trueCount = runningCount / (cardsInDeck / 52)
    cardsInDeck = cardsInDeck - 1
    GPIO.output(25,GPIO.LOW)
    print('high ',runningCount, trueCount)
    time.sleep(1)

def init():
  GPIO.output(25,GPIO.LOW)
  GPIO.output(17,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)
  GPIO.output(22,GPIO.LOW)

  time.sleep(2)

  GPIO.output(17,GPIO.HIGH)
  GPIO.output(27,GPIO.HIGH)
  GPIO.output(22,GPIO.HIGH)

  time.sleep(1)

  GPIO.output(17,GPIO.LOW)

  time.sleep(1)

  GPIO.output(27,GPIO.LOW)

  time.sleep(1)

  GPIO.output(22,GPIO.LOW)

  time.sleep(2)
init()

while True:
  main()

  #
