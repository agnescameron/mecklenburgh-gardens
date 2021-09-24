import os
import time
import helpers
import itertools
import csv
from operator import itemgetter
import random
import json
import scipy.stats as scipy

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
		self.years = {}
		print('initialising')
		# choose a random scenario
		self.scen_name, scen_list = random.choice(list(projection_data.items()))
		# print(json.dumps(self.scenario, indent=2))
		# print(self.scenario[0], json.dumps(self.scenario[1], indent=2))
		# output a list of projected 
		for period, period_list in scen_list.items():
			start, end = period.split('-')

			for year in int(start), int(end):
				self.years[year] = {}
				for season, dist in period_list.items():
					self.years[year][season] = helpers.norm_from_percentiles(
							float(dist["10_perc"]), 0.1, float(dist["90_perc"]), 0.9
						)
					# print(self.years[year][season].rvs(size=1))


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
			projections[scen_name][year] = {}
			for period in year_group:
				print(period["variable"])
				projections[scen_name][year][period["variable"]] = {
						"5_perc": period["5_perc"],
						"10_perc": period["10_perc"],
						"50_perc": period["50_perc"],
						"90_perc": period["90_perc"],
						"95_perc": period["95_perc"]
				}


	return projections






