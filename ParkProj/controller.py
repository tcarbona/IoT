import RPi.GPIO as GPIO
import time
import sys
import requests


GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit1 = 7
pin_to_circuit2 = 13
pin_to_circuit3 = 29
pin_to_circuit4 = 37
s1 = 0 
s2 = 0
s3 = 0
s4 = 0


def rc_time (pin_to_circuit):
    count = 0
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
      #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count


def runController():
#Catch when script is interupted, cleanup correctly
    # Main loop
   while True:
#       setCurrentState('state')

       if rc_time(pin_to_circuit1) > 5000:
        #Spot 1
         s1 = 1 
#         setCurrentState('state9')
       else:
         s1 = 0

       if rc_time(pin_to_circuit2) > 5000:
        #Spot 2 is taken
         s2 = 1
       else:
        #Spot 2 available
         s2 = 0
 
       if rc_time(pin_to_circuit3) > 5000:
        #Spot 3 is taken
         s3 = 1
       else:
        #Spot 3 available
         s3 = 0

       if rc_time(pin_to_circuit4) > 5000:
        #Spot 4 is taken
         s4 = 1
 #        setCurrentState('state1')
       else:
        #Spot 4 available
         s4 = 0

       if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
         setCurrentState('state0')
       elif s1 == 0 and s2 == 0 and s3 == 0 and s4 == 1:
         setCurrentState('state1')
       elif s1 == 0 and s2 == 0 and s3 == 1 and s4 == 0:
         setCurrentState('state2')
       elif s1 == 0 and s2 == 0 and s3 == 1 and s4 == 1:
         setCurrentState('state3')
       elif s1 == 0 and s2 == 1 and s3 == 0 and s4 == 0:
         setCurrentState('state4')
       elif s1 == 0 and s2 == 1 and s3 == 0 and s4 == 1:
         setCurrentState('state5')
       elif s1 == 0 and s2 == 1 and s3 == 1 and s4 == 0:
         setCurrentState('state6')
       elif s1 == 0 and s2 == 1 and s3 == 1 and s4 == 1:
         setCurrentState('state7')
       elif s1 == 1 and s2 == 0 and s3 == 0 and s4 == 0:
         setCurrentState('state8')
       elif s1 == 1 and s2 == 0 and s3 == 0 and s4 == 1:
         setCurrentState('state9')
       elif s1 == 1 and s2 == 0 and s3 == 1 and s4 == 0:
         setCurrentState('state10')
       elif s1 == 1 and s2 == 0 and s3 == 1 and s4 == 1:
         setCurrentState('state11')
       elif s1 == 1 and s2 == 1 and s3 == 0 and s4 == 0:
         setCurrentState('state12')
       elif s1 == 1 and s2 == 1 and s3 == 0 and s4 == 1:
         setCurrentState('state13')
       elif s1 == 1 and s2 == 1 and s3 == 1 and s4 == 0:
         setCurrentState('state14')
       elif s1 == 1 and s2 == 1 and s3 == 1 and s4 == 1:
         setCurrentState('state15')
       else:
         setCurrentState('Unknown')
       time.sleep(2)

def setCurrentState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/state/1/', data=values,
                     auth=('pi', 'tomtom'))

while True:
    try:
        runController()
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

