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
green_stobe = "140000001F10500000000000000000000"
