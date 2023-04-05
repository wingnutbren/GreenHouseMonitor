#gpiostub

# a do-nothing stub that will be used when NOT on a device with GPIO pins
# you should not expect anything to work in this case

HIGH = 1
LOW = 0
BCM = 1101
IN = 1
OUT = 2

def output(pin,state):
    ...
    # print('running output function')

def input(pin):
    ...
    # print('running input function')


def setmode( mode):
    ...
    # print('running setmode function')


def setwarnings(mode):
    ...
    # print('running setwarnings function')


def setup(a,b):
    ...
    # print('running setup function')

 
