import numpy as np
import os
import time
import helpers
import itertools
import csv
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
		# 

		# output a list of projected 


def initialise_projection_data():
	with open('./assets/external_data/london_climate.csv', 'r') as file:
		all_ = list(csv.DictReader(file))

	projections = {}
	for scenario, scen_group in itertools.groupby(
			all_, 
			key=lambda r: (r['emissions'])):
		print('scenario is', scenario)
		projections[scenario] = {}
		for year, year_group in itertools.groupby(
				scen_group, 
				key=lambda r: (r['time'])):
				for period in year_group:
					projections[scenario][year] = {
						period["variable"]: {
							"5_perc": period["5_perc"],
							"10_perc": period["10_perc"],
							"50_perc": period["50_perc"],
							"90_perc": period["90_perc"],
							"95_perc": period["95_perc"]
						}
					}

	return projections






