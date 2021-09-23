# from scipy.stats import skewnorm
import numpy
import json
import csv

def get_json(obj):
	return json.loads(
		json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o)))
	)

def json_from_data(file):
	result = []

	csv_reader = csv.DictReader(file)
	for row in csv_reader:
		result.append(row)


	return result