import os

dirname = os.path.dirname(__file__)

class Park:
	plants = []
	animals = []
	segments = []

class Plant:
	def __init__(self, type, id, temp_mean, temp_std, water_mean, water_std):
		print('plant')

class Animal:
	def __init__(self, type, id, desired_habitat):
		#animals
		print('animal')


class Segment:
	def __init__(self, type, id, contents):
		print('segment')


def update(day, climate_state):
	print('updating state of park', day, climate_state.water)


def initialise():
	print('updating state of park')


def add_plant():
	print('adding plant')


def plant_death():
	print('plant death')