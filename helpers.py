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
	# headers = list(map(lambda header: header.replace(" ", "_").lower(), headers))
	# print(headers)

	# del data[0]

	# for row in data:
	# 	obj = {}
	# 	for i, header in enumerate(headers):
	# 		try:
	# 			obj[header] = row[i]
	# 		except:
	# 			obj[header] = ""
	# 	result.append(obj)


	csv_reader = csv.DictReader(file)
	#convert each csv row into python dict
	for row in csv_reader:
		print('aaa', row)
		#add this python dict to json array
		result.append(row)


	return result