import os
import time

class Climate:
	rain = 'rain'
	water = 'water'

# river fleet?
class Water:
	print('water')

# world always loads same state from climate
# info files
def initialise():
	print('initialising climate')

climate = Climate()

def update(day):
	print('initialising climate', day)
	return climate