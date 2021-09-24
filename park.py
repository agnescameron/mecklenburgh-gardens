import os
import json
import csv
import helpers

dirname = os.path.dirname(__file__)

class Park:

	def __init__(self):
		self.trees = self.create_trees()
		self.possible_events = self.create_possible_events()

	def create_possible_events(self):
		with open('./assets/garden_index/events.csv') as file:
			possible_events = helpers.json_from_data(file)
			print(possible_events)
			return possible_events

	def create_trees(self):
		trees_list = []
		with open(r'./assets/external_data/tree_info.csv') as file:
			tree_info = helpers.json_from_data(file)

		with open('./assets/garden_index/trees.csv') as file:
			reader = csv.reader(file)
			for row in reader:
				try:
					tree = list(filter(lambda x:x["name"]==row[1], tree_info))[0]
					trees_list.append(Tree(tree, row[0], row[2], row[3], row[4], row[5]))
				except:
					print('tree not in list')

		return trees_list

	def update_month(self, climate_state):
		print('updating state of park')
		self.events = []

		for event in self.possible_events:
			print(event)
			# self.events.append({
			# 	'day': 3,
			# 	'text': 'another day in the park'
			# 	})

		self.park_welfare(climate_state)

	def park_welfare(self, climate_state):
		for tree in self.trees:
			print(tree.print())

	def get_events(self, day):
		event_list = []

		for event in self.events:
			if event["day"] == day.day: event_list.append(event)

		return event_list


	def get_season(self, day):
		if day.month in [9, 10, 11]:
			return 'autumn'
		elif day.month in [12, 1, 2]:
			return 'winter'
		elif day.month in [3, 4, 5]:
			return 'spring'
		else:
			return 'summer'

	def outbreak(self):
		print('adding plant')

	def add_plant(self):
		print('adding plant')

	def get_park(self):
		return helpers.get_json(self)


class Tree:
	def __init__(self, info, id, x_pos, y_pos, radius, age):
		# print('tree')
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


def create_segments():
	segments = ['seg', 'seg']
	return segments
