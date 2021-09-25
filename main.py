import time
import os
import concurrent.futures
import json
from datetime import date, timedelta
# from dateutil.relativedelta import relativedelta
from calendar import monthrange

# submodules
import server
import park
import climate

dirname = os.path.dirname(__file__)
db_file = os.path.join(dirname, 'meck.db')
start_date = date(2021, 9, 25)
# sim_length = 99
speed = 0.4

def init_db():
	global db_file
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		c=conn.cursor()
		c.execute('''DROP TABLE IF EXISTS park''')
		c.execute('''CREATE TABLE IF NOT EXISTS park
			(id INTEGER PRIMARY KEY, 'timestamp' DATETIME DEFAULT 
			CURRENT_TIMESTAMP, temp TEXT, monthnum INT, entityType TEXT)''')
		print(sqlite3.version)
	except sqlite3.Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

def wrap_up():
	#resolve simulation after 100 / (?50?) years
	#does this happen periodically anyway?
	#write out the results of the simulation to database
	print('recording results')
	# record_results()

def advance_month(day):
	#calculate the season
	global park_state, climate_state

	print("Month", day.month)
	month_length = monthrange(day.year, day.month)[1]
	#calculate the temperature, pollution, other stats

	climate_state.update(day)
	park_state.update_month(climate_state, month_length)

	# go over each day in months and put the events on them
	for day_num in range(day.day, month_length+1):
		day = day + timedelta(days=1)
		events = park_state.get_events(day)
		for event in events:
			print(day, event["text"])
		server.update_park(park_state)
		time.sleep(1/speed)

	return day

def initialise():
	global park_state, climate_state

	climate_state = climate.Climate(projection_data, baseline_data)
	park_state = park.Park(start_date)


def run_simulation():
	day = start_date
	year = day.year
	initialise()

	while year < 2099:
		day = advance_month(day)
		year = day.year

	wrap_up()

def main_loop():
	global projection_data, baseline_data

	sim_num = 0
	projection_data = climate.initialise_projection_data()
	baseline_data = climate.initialise_baseline()

	while True:
		print('initialising simulation', sim_num)
		run_simulation()
		sim_num +=1

def run_jobs(executor):
	app = executor.submit(server.run)
	sim = executor.submit(main_loop)
	return app, sim

if __name__ == "__main__":
	# init_db()

	futures = run_jobs(concurrent.futures.ThreadPoolExecutor(max_workers = 2))
	
	for job in concurrent.futures.as_completed(futures):
		print(job.result())
