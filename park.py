import os
import json
import csv
import helpers

dirname = os.path.dirname(__file__)

class Park:
	events = []

	def __init__(self, plants, animals, segments):
		print('plant')
		self.plants = plants
		self.animals = animals
		self.segments = segments

	def update(self, day, climate_state):
		print('updating state of park')
		events.append('another day in the park')
		for plant in self.plants:
			print(plant.full_name)

	def outbreak(self):
		print('adding plant')

	def add_plant(self):
		print('adding plant')

	def get_park(self):
		return helpers.get_json(self)


class Tree:
	def __init__(self, info, id, x_pos, y_pos, radius, age):
		print('tree')
		for key, val in info.items():
			setattr(self, key, val)
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.radius = radius
		self.age = age

	def progress_disease(self):
		print('tree has disease')

	def age(self):
		print('tree dying')

	def die(self):
		print('tree dying')

	def print(self):
		return helpers.get_json(self)


class Plant:
	def __init__(self, type, id, temp_mean, temp_std, water_mean, water_std):
		print('plant')

	def die(self):
		print('animal dying')

	def print(self):
		return helpers.get_json(self)


class Animal:
	def __init__(self, type, id, desired_habitat):
		#animals
		print('animal')

	def mate(self):
		print('mating')

	def die(self):
		print('animal dying')

	def print(self):
		return helpers.get_json(self)


class Segment:
	def __init__(self, state):
		print('segment')

	def print(self):
		return helpers.get_json(self)


def create_plants():
	plants = []
	plant_info = json.loads(open('./assets/plant_info.json').read())

	with open('./assets/tree_index.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				tree_info = plant_info[row[1]]
				tree = Tree(tree_info, row[0], row[2], row[3], row[4], row[5])
				plants.append(tree)
			except:
				print('tree not in list')
	print(plants)

	return plants


def create_animals():
	# animal generation
	animals = ['animal']
	return animals


def create_segments():
	segments = ['seg', 'seg']
	return segments
