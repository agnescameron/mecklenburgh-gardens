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

	def __init__(self, projection_data, baseline_data):
		self.baseline = baseline_data
		self.projection = {}
		print('initialising')
		# choose a random scenario
		self.scen_name, scen_list = random.choice(list(projection_data.items()))

		# output a list of projected distributions
		for period, period_list in scen_list.items():
			start, end = period.split('-')

			for year in range(int(start), int(end)):
				self.projection[year] = {}
				# if time, perturb this according to second norm
				for season, dist in period_list.items():
					self.projection[year][season] = helpers.norm_from_percentiles(
							float(dist["10_perc"]), 0.1, float(dist["90_perc"]), 0.9
						)

	def get_season(self, day):
		if day.month in [9, 10, 11]:
			return 'autumn'
		elif day.month in [12, 1, 2]:
			return 'winter'
		elif day.month in [3, 4, 5]:
			return 'spring'
		else:
			return 'summer'

	def get_cli_season(self, day):
		if day.month in [10, 11, 12, 1, 2, 3]:
			return 'winter'
		else:
			return 'summer'

	def update(self, day):
		season = self.get_cli_season(day)
		projection = self.projection[day.year]
		baseline = self.baseline[day.month-1]

		precip = projection[season + "_precip"].rvs(size=1)[0]*float(baseline["precip"])*0.01 + float(baseline["precip"])
		max_temp = projection[season + "_temp"].rvs(size=1)[0] + float(baseline["max_temp"])
		min_temp = projection[season + "_temp"].rvs(size=1)[0] + float(baseline["min_temp"])
		print("this week's weather", day, baseline["month"], "precipitation is", precip/4, "max temp is", max_temp, "min temp is",min_temp)


	def print(self):
		return helpers.get_json(self)

def initialise_baseline():
	with open('./assets/external_data/london_baseline.csv', 'r') as file:
		all_ = list(csv.DictReader(file))
		return all_

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
				projections[scen_name][year][period["variable"]] = {
						"5_perc": period["5_perc"],
						"10_perc": period["10_perc"],
						"50_perc": period["50_perc"],
						"90_perc": period["90_perc"],
						"95_perc": period["95_perc"]
				}


	return projections






