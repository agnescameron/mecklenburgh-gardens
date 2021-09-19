import time
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

# submodules
import server
import park
import climate

dirname = os.path.dirname(__file__)
db_file = os.path.join(dirname, 'meck.db')
start_date = date(2021, 9, 25)
sim_length = 3
speed = 1

def init_db():
	global db_file
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		c=conn.cursor()
		c.execute('''DROP TABLE IF EXISTS park''')
		c.execute('''CREATE TABLE IF NOT EXISTS park
			(id INTEGER PRIMARY KEY, 'timestamp' DATETIME DEFAULT CURRENT_TIMESTAMP, temp TEXT, monthnum INT, entityType TEXT)''')
		print(sqlite3.version)
	except sqlite3.Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

def record_results():
	#write out the results of the simulation to database
	print('recording results')

def wrap_up():
	#resolve simulation after 100 / (?50?) years
	#does this happen periodically anyway?
	record_results()

def advance_day(day):
	#calculate the season
	global park_state, climate_state
	print('advancing day')

	#calculate the temperature, pollution, other stats
	day = day + timedelta(days=7)
	climate_state.update(day)
	park_state.update(day, climate_state)
	print('day is', day, 'year is', day.year)
	return day

def initialise():
	global park_state, climate_state
	print('initialising park')

	# park.create_park()
	plants = park.create_plants()
	animals = park.create_animals()
	segments = park.create_segments()

	park_state = park.Park(plants, animals, segments)
	climate_state = climate.Climate('heavy')


def run_simulation():
	day = start_date
	year = day.year
	initialise()

	while year < start_date.year + sim_length:
		day = advance_day(day)
		year = day.year
		time.sleep(1/speed)

	wrap_up()

def main_loop():
	sim_num = 0
	while True:
		print('initialising simulation', sim_num)
		run_simulation()
		sim_num +=1
	# keep running 100-year cycles

if __name__ == "__main__":
	print('starting sim')
	# init_db()

	# executor = ThreadPoolExecutor(max_workers=3)
	# app = executor.submit(server.run)
	# sim = executor.submit(main_loop)

	main_loop()