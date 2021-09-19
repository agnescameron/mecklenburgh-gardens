import numpy as np
import os
import time

class Climate:
	rain = 'rain'
	water = 'water'

	def __init__(self, emissions_scenario):
		self.emissions = emissions_scenario

	def update(self, day):
		print('updating climate', day)

# river fleet?
class Water:
	print('water')

# # world always loads same state from climate
# # info files
# def initialise():
# 	print('initialising climate')

# def initialise():