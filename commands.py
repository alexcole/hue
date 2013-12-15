import constants
import requests
import json


def set_light_state(number, data):
	jsondata = json.dumps(data)
	url = constants.base_url+"lights/%s/state" % str(number)
	r = requests.put(url, data=jsondata)
	return r.text


def color_loop(number):
	return set_light_state(number, {"effect": "colorloop"})

def off(number):
	return set_light_state(number, {"on":False})

def on(number):
	return set_light_state(number, {"on":True})


def all_lights(f, *args):
	result = []
	for i in constants.numbers:
		result.append(f(i, *args))
	return result