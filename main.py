import time
import os
# import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

# submodules
import server
import park
import climate

dirname = os.path.dirname(__file__)
db_file = os.path.join(dirname, 'meck.db')
start_date = date(2021, 9, 25)

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
	#calculate the temperature, pollution, other stats
	day = day + timedelta(days=7)
	print('day is', day, 'year is', day.year)
	time.sleep(0.001)
	return day

def run_simulation():
	# #initial setup
	# park.create_park()
	# climate.initialise_climate()
	# climate.perturb_model() # no feedback from garden to climate?
	day = start_date
	year = day.year

	while year < 2121:
		day = advance_day(day)
		year = day.year
	wrap_up()

def main_loop():
	simnum = 0
	while True:
		print('starting simulation', simnum)
		run_simulation()
		simnum +=1
	# keep running 100-year cycles

if __name__ == "__main__":
	print('starting sim')
	# init_db()

	executor = ThreadPoolExecutor(max_workers=3)
	app = executor.submit(server.run)
	sim = executor.submit(main_loop)

