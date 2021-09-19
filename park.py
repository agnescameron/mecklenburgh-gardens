import os
import json
import csv

dirname = os.path.dirname(__file__)

class Park:
	def __init__(self, plants, animals, segments):
		print('plant')
		self.plants = plants
		self.animals = animals
		self.segments = segments

	def update(self, day, climate_state):
		print('updating state of park')
		for plant in self.plants:
			print(plant.full_name)

	def outbreak(self):
		print('adding plant')

	def add_plant(self):
		print('adding plant')


class Tree:
	def __init__(self, info, id, x_pos, y_pos, radius, age):
		print('tree')
		for key, val in info.items():
			setattr(self, key, val)
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.radius = radius
		self.age = age

	def die(self):
		print('animal dying')

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
	return plants


def create_animals():
	animals = ['animal']
	return animals


def create_segments():
	segments = ['seg', 'seg']
	return segments
