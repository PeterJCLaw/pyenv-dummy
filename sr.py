'''
This is a dummy implementation of the SR API, as documented at:
* http://trac.srobo.org/wiki/RobotAPI
* http://srobo.org/docs/programming/
This should not be considered canonical!
'''

# Imports
from collections import namedtuple as _namedtuple

# Constants
MARKER_ARENA = 13
MARKER_ROBOT = 13
MARKER_SLOT = 13
MARKER_TOKEN_TOP = 13
MARKER_TOKEN_BOTTOM = 13
MARKER_TOKEN_SIDE = 13

INPUT = "INPUT"
OUTPUT = "OUTPUT"
INPUT_PULLUP = "INPUT_PULLUP"

# Power

class Battery:
    def __init__(self):
        self.voltage = 12.3
        self.current = 1.3

class Power:
    def __init__(self):
        self.led = [0,1,2,3,4,5,6,7]
        self.battery = Battery()

    def beep(self, hz, time=1):
        pass

# Vision

MarkerInfo = _namedtuple( "MarkerInfo", "code marker_type offset size" )
ImageCoord = _namedtuple( "ImageCoord", "x y" )
WorldCoord = _namedtuple( "WorldCoord", "x y z" )
PolarCoord = _namedtuple( "PolarCoord", "length rot_x rot_y" )
Orientation = _namedtuple( "Orientation", "rot_x rot_y rot_z" )
Point = _namedtuple( "Point", "image world polar" )

class Marker:
    def __init__(self):
        # Aliases
        self.info = MarkerInfo()
        self.timestamp = 3.14159
        self.res = (800, 600)
        self.vertices = []
        self.centre = Point()
        self.dist = 42
        self.rot_y = 13
        self.orientation = Orientation()

# Logic Expressions

def And(*args):
    return args

def Or(*args):
    return args

# Robot

class Robot:
    def __init__(self):
        self.usbkey = None
        self.startfifo = None
        self.mode = None
        self.zone = None
        self.motors = []
        self.ruggeduinos = []
        self.power = Power()
        self.servos = []

    def see(self, res = (800, 600), stats = False):
        """
        Make the robot see stuff
        """
        return [Marker()]
