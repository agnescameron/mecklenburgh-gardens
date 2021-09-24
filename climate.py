import os
import time
import helpers
import itertools
import csv
from operator import itemgetter
import random
import json

class Climate:
	rain = 'rain'
	water = 'water'

	def __init__(self, emissions_scenario):
		self.emissions = emissions_scenario

	def update(self, day):
		# print('updating climate', day)
		pass

# river fleet?
class Water:
	print('water')

# # world always loads same state from climate
# # info files
# def initialise():
# 	print('initialising climate')

class Projection:
	def __init__(self, projection_data):
		print('initialising')
		# choose a random scenario
		self.scenario = random.choice(list(projection_data.items()))
		# print(json.dumps(self.scenario, indent=2))
		# print(self.scenario[0], json.dumps(self.scenario[1], indent=2))
		# output a list of projected 
		for period in self.scenario[1].items():
			start, end = period[0].split('-')
			# dist = helpers.norm_from_percentiles()

			# for year in 


			print(start, end)


def initialise_projection_data():
	with open('./assets/external_data/london_climate.csv', 'r') as file:
		all_ = list(csv.DictReader(file))

	scen_groups = {}
	for scen_name, scen_group in itertools.groupby(
			all_, 
			key=lambda r: (r['emissions'])):
		scen_groups[scen_name] = sorted(list(scen_group), key = itemgetter('time'))

	projections = {}
	for scen_name, scen_details in scen_groups.items():
		projections[scen_name] = {}
		for year, year_group in itertools.groupby(
				scen_details, 
				key=lambda t: (t['time'])):
			for period in year_group:
				projections[scen_name][year] = {
					period["variable"]: {
						"5_perc": period["5_perc"],
						"10_perc": period["10_perc"],
						"50_perc": period["50_perc"],
						"90_perc": period["90_perc"],
						"95_perc": period["95_perc"]
					}
				}

	return projections






