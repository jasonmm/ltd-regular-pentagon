"""
LTD Puzzle 2: Regular Pentagon
From: http://forum.lessthandot.com/viewtopic.php?f=102&t=1724

Given a grid co-ordinate (x,y) as the centre point of a regular pentagon, and 
the sum of the length of the sides, return the co-ordinates of each point as: 
"Top", "MidLeft", "MidRight", "BottomLeft", "BottomRight" and the distance 
from the centre to each of the points.
"""

import argparse
import string
import math


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return( str(round(self.x,3))+","+str(round(self.y,3)) )

class RegularPentagon:
    top = Point(0,0)
    mid_left = Point(0,0)
    mid_right = Point(0,0)
    bottom_right = Point(0,0)
    bottom_left = Point(0,0)
    sides = 5

    def __init__(self):
        pass



parser = argparse.ArgumentParser(description="Regular Pentagon", add_help=True)
parser.add_argument("center", metavar="center", default="0,0", help="The x,y coordinate of the center of a regular pentagon.")
parser.add_argument("perimeter", metavar="perimeter", help="The length of the perimeter of the regular pentagon.")
args = parser.parse_args()

pentagon = RegularPentagon()

# Calculate some initial values
side_length = float(args.perimeter)/pentagon.sides
center_point = string.split(args.center, ",")
center = Point(float(center_point[0]), float(center_point[1]))
apothem = side_length / (2*math.tan(math.radians(180/pentagon.sides)))

# Some convenience variables
sin54 = math.sin(math.radians(54))
sin72 = math.sin(math.radians(72))
sin90 = math.sin(math.radians(90))

# The radius of circumcircle.
radius = side_length / ( sin54 + sin72 )

# Find top point.
pentagon.top = Point(center.x, center.y+radius)

# Find mid- points.
run = (side_length * sin54) / sin90
rise = (side_length * math.sin(math.radians(36))) / sin90
pentagon.mid_right = Point(pentagon.top.x+run, pentagon.top.y-rise)
pentagon.mid_left = Point(pentagon.top.x-run, pentagon.top.y-rise)

# Find bottom- points.
run = side_length/2;
rise = apothem
pentagon.bottom_right = Point(center.x+run, center.y-rise)
pentagon.bottom_left = Point(center.x-run, center.y-rise)

# Calculate the area
area = (float(args.perimeter)*apothem)/2

# Output
print "Top: "+str(pentagon.top)
print "Mid-Right: "+str(pentagon.mid_right)
print "Mid-Left: "+str(pentagon.mid_left)
print "Bottom-Right: "+str(pentagon.bottom_right)
print "Bottom-Left: "+str(pentagon.bottom_left)

print "Area: "+str(area)
 




