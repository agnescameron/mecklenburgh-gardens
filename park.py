import os
import json
import csv
import helpers
import numpy as np
import random

dirname = os.path.dirname(__file__)

class Park:

	def __init__(self, day):
		self.trees = self.create_trees()
		self.possible_events = self.create_possible_events()
		self.day = day
		self.day_events = []

	def create_possible_events(self):
		with open(os.path.join(dirname, './assets/garden_index/events.csv')) as file:
			possible_events = helpers.json_from_data(file)

		return possible_events

	def create_trees(self):
		trees_list = []
		with open(os.path.join(dirname, './assets/external_data/tree_info.csv')) as file:
			tree_info = helpers.json_from_data(file)

		with open(os.path.join(dirname,'./assets/garden_index/trees.csv')) as file:
			reader = csv.reader(file)
			for row in reader:
				try:
					tree = list(filter(lambda x:x["name"]==row[1], tree_info))[0]
					trees_list.append(Tree(tree, row[0], row[2], row[3], row[4], row[5]))
				except:
					print(row[1], 'tree not in list')

		return trees_list

	def update_month(self, climate_state, month_length):
		print('updating state of park')
		self.month_events = []
		weather = climate_state.print()
		print("precip is", weather["precip"])

		for event in self.possible_events:
			mu = float(event["baseline_freq"])

			if event["type"] == "precip":
				if event["subtype"] == "high" and weather["precip"] > float(event["threshold"]):
					mu = float(event["baseline_freq"]) + (weather["precip"] 
						- float(event["threshold"]))*float(event["multiplier"])

				elif event["subtype"] == "low" and weather["precip"] < float(event["threshold"]):
					mu = float(event["baseline_freq"]) + ( float(event["threshold"]) 
						- weather["precip"])*float(event["multiplier"])

			elif event["type"] == "temp":
				if event["subtype"] == "high" and weather["max_temp"] > float(event["threshold"]):
					print("weather and event is", weather["max_temp"], float(event["threshold"]))
					mu = float(event["baseline_freq"]) + (weather["max_temp"] 
						- float(event["threshold"]))*float(event["multiplier"])

				elif event["subtype"] == "low" and weather["min_temp"] < float(event["threshold"]):
					mu = float(event["baseline_freq"]) + ( float(event["threshold"]) 
						- weather["min_temp"])*float(event["multiplier"])

			num_event = np.random.poisson(mu)
			print(event["name"], "normally happens", 
				float(event["baseline_freq"]), "but now", num_event)

			days = random.sample(range(1, month_length+1), num_event)

			for inst in range(0, num_event):
				self.month_events.append({
					"name": event["name"],
					"text": event["text"],
					"effect": event["effects"],
					"day": days[inst]
				})

		self.park_welfare(climate_state)

	def park_welfare(self, climate_state):
		for tree in self.trees:
			# check against climate
			# append tree welfare to events (at random, apart from death)
			pass

	def get_events(self, day):
		self.day = day
		self.day_events = []

		for event in self.month_events:
			if event["day"] == day.day: 
				self.day_events.append(event)

		return self.day_events


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


