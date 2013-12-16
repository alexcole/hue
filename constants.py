# This defintes the ip_address and username
from secrets import *

base_url = "http://%s/api/%s/" % (ip_address, username)

numbers = [1, 2, 3]

default_transition_time = 4

maxbri = 255
halfbri = 127
minbri = 0


maxsat = 255
halfsat = 127
minsat = 0


# Colors!
minhue = 0
red = 0
green = 25500
blue = 46920
maxhue = 65535


# Stobe values (very sketchy)
# I think we can trim these more. Not sure what the 'correct' length is
# When they are too short, it doesnt store the new one
green_stobe =   "140000001F105000000000000000000000000000"
red_strobe =    "140000001F100000000000000000000000000000"
orange_strobe = "140000001F100500000000000000000000000000"
blue_strobe =   "14000000FF000030000000000000000000000000"
purple_strobe = "14000000FF100030000000000000000000000000"
blue_green =    "14000000FF00FF10000000000000000000000000"