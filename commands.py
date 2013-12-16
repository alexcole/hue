from constants import *
import requests
import json
import random
import time

def set_light_state(number, data):
	jsondata = json.dumps(data)
	url = base_url+"lights/%s/state" % str(number)
	return requests.put(url, data=jsondata).text

def color_loop(number):
	return set_light_state(number, {"effect": "colorloop"})

def stop_color_loop(number):
	return set_light_state(number, {"effect": "none"})

def off(number):
	return set_light_state(number, {"on":False})

def on(number):
	return set_light_state(number, {"on":True})


def breath(number):
	return set_light_state(number, {"alert":"select"})

def color(number, hue, sat, bri, time=4):
	return set_light_state(number, {"hue":hue, "sat":sat, "bri": bri, "transitiontime": time})

def random_color(number, time):
	hue = random.randint(minhue, maxhue)
	color(number, hue, maxsat, maxbri, time=time)

def rave():
	while True:
		for i in numbers:
			random_color(i, 0)
			time.sleep(.05)



def strobe(ms):
	# THis is dark magic from http://weblog.lmeijer.nl/archives/225-Do-hue-want-a-strobe-up-there.html

	# Set up point symbol on all lights
	point_symbol = json.dumps({"1":"0A00F1F01F1F1001F1FF100000000000000"})
	for i in numbers:
		url = base_url+"lights/%s/pointsymbol" % str(i)
		requests.put(url, data=point_symbol)

	# Start it using group 0
	data = json.dumps({"symbolselection":"01010501010102010301040105","duration":ms})
	url = base_url+"groups/0/transmitsymbol"
	return requests.put(url, data=data).text




def strobe2(foo, ms):
	# THis is dark magic from http://weblog.lmeijer.nl/archives/225-Do-hue-want-a-strobe-up-there.html

	# Set up point symbol on all lights
	point_symbol = json.dumps({"1":foo})
	for i in numbers:
		url = base_url+"lights/%s/pointsymbol" % str(i)
		print requests.put(url, data=point_symbol).text

	# Start it using group 0
	data = json.dumps({"symbolselection":"01010501010102010301040105","duration":ms})
	url = base_url+"groups/0/transmitsymbol"
	return requests.put(url, data=data).text

def color_strobe(ms, speed, red, green, blue):
	"""
	Red, green, and blue are strings from '00' to 'FF'
	Speed is a string from '04' to '30' (ish)
	"""

	point_symbol = json.dumps({"1":"%s000000FF%s%s%s000000000000000000000000" % (speed, red, green, blue)})
	for i in numbers:
		url = base_url+"lights/%s/pointsymbol" % str(i)
		requests.put(url, data=point_symbol)

	# Start it using group 0
	data = json.dumps({"symbolselection":"01010501010102010301040105","duration":ms})
	url = base_url+"groups/0/transmitsymbol"
	return requests.put(url, data=data).text





def all_lights(f, *args, **kwargs):
	"""
	Runs f in the background on all the lights
	"""
	answer = []
	for i in numbers:
		answer.append(f(i, *args, **kwargs))
	return answer