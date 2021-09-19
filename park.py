import os

dirname = os.path.dirname(__file__)

class Park:
	def __init__(self, plants, animals, segments):
		print('plant')
		self.plants = plants
		self.animals = animals
		self.segments = segments

	def update(self, day, climate_state):
		print('updating state of park', day, climate_state.water)

	def outbreak(self):
		print('adding plant')

	def add_plant(self):
		print('adding plant')


class Plant:
	def __init__(self, type, id, temp_mean, temp_std, water_mean, water_std):
		print('plant')

	def die(self):
		print('animal dying')

class Animal:
	def __init__(self, type, id, desired_habitat):
		#animals
		print('animal')

	def mate(self):
		print('mating')

	def die(self):
		print('animal dying')


class Segment:
	def __init__(self, state):
		print('segment')


def create_plants():
	plants = ['tree', 'tree', 'tree']
	return plants


def create_animals():
	animals = ['animal']
	return animals


def create_segments():
	segments = ['seg', 'seg']
	return segments
