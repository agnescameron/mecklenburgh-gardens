# from scipy.stats import skewnorm
import numpy as np
import json
import csv
from scipy.stats import norm, lognorm, poisson

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

def norm_from_percentiles(x1, p1, x2, p2):
	""" Return a normal distribuion X parametrized by:
		P(X < p1) = x1
		P(X < p2) = x2
	"""
	p1ppf = norm.ppf(p1)
	p2ppf = norm.ppf(p2)

	location = ((x1 * p2ppf) - (x2 * p1ppf)) / (p2ppf - p1ppf)
	scale = (x2 - x1) / (p2ppf - p1ppf)

	return norm(loc=location, scale=scale)

def lognorm_from_percentiles(x1, p1, x2, p2):
	""" Return a log-normal distribuion X parametrized by:
		P(X < p1) = x1
		P(X < p2) = x2
	"""
	x1 = np.log(x1)
	x2 = np.log(x2)
	p1ppf = norm.ppf(p1)
	p2ppf = norm.ppf(p2)

	scale = (x2 - x1) / (p2ppf - p1ppf)
	mean = ((x1 * p2ppf) - (x2 * p1ppf)) / (p2ppf - p1ppf)

	return lognorm(s=scale, scale=np.exp(mean))


def sample_norm(dist):

	return numpy.random.normal(dist.loc, dist.scale)

