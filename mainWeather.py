import sqlite3
import json
import requests

def main():

	db_connection = sqlite3.connect('databaseWeather/projWeather.sqlite3')
	db_connection.row_factory = dict_factory

#****************************** API SETUP ******************************
	#Dark Sky API Setup
	urlDS = 'https://api.darksky.net/forecast/'
	keyDS = '32849631c035aed991cf0e243adf6250'
	

	#Windly API Setup
	urlW = 'TBD'
	keyW = '9YxsexFTYueoaYEkhbH4mTPbocLl1LLb'


	#Global API Setup Variables
	#Stevens Pass - STP
	latitudeSTP_base = '47.7456352'
	longitudeSTP_base = '-121.0891718'
	elevationMTB_base = 1240


	#Mt. Baker - MTB
	latitudeMTB_base = '48.8616632'
	longitudeMTB_base = '-121.6537997'
	elevationMTB_base = 1107

	#Crystal - CRL
	latitudeCRL_base = '46.93604621378571'
	longitudeCRL_base = '-121.47433662466939'
	elevationCRL_base = 1337

	#Home - HOM
	latitudeHOM = '47.6603834'
	longitudeHOM = '-122.3557788'
	elevationHOM = 75

#****************************** API CALLS ******************************
	rSTP = requests.get(url=urlDS+keyDS+'/'+latitudeSTP_base+','+longitudeSTP_base)
	rMTB = requests.get(url=urlDS+keyDS+'/'+latitudeMTB_base+','+longitudeMTB_base)
	rCRL = requests.get(url=urlDS+keyDS+'/'+latitudeCRL_base+','+longitudeCRL_base)
	rHOM = requests.get(url=urlDS+keyDS+'/'+latitudeHOM+','+longitudeHOM)
	#rW = requests.get(url=urlW+keyW+'/'+)
	#data = db_connection.execute("SELECT ")

#******************* Extract data from API into db *************
	API2db(rSTP.json(), db_connection, 'STP')
	API2db(rMTB.json(), db_connection, 'MTB')
	API2db(rCRL.json(), db_connection, 'CRL')
	API2db(rHOM.json(), db_connection, 'HOM')

#******************* Print Report *************

	printSnowReport(db_connection)



#Converts the query in the database into a python dictionary so that you can index into it easier
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


#Takes in a temperature in C as input, outputs the temperature in F
def celsius2fahrenheit(temp):
	return (temp * 9 / 5) + 32

#Takes in an API call from Dark Sky and puts info into database
#Inputs: API call, database name
def API2db(r, db, loc):
	data = db.execute("SELECT id FROM weather ORDER BY id DESC").fetchall()
	rid = ''
	if data == []:
		rid = 0
	else:
		rid = data[0]['id'] + 1

	rtimeId = r['hourly']['data'][0]['time']
	rlatitude = r['latitude']
	rlongitude = r['longitude']
	rlocation = loc
	rsummaryForcast = r['hourly']['summary']
	rcurTemp = r['hourly']['data'][0]['temperature']

	db.execute("INSERT INTO weather(id, timeId, latitude, longitude, location, summaryForcast, curTemp) VALUES(?,?,?,?,?,?,?)", [rid, rtimeId, rlatitude, rlongitude, rlocation, rsummaryForcast, rcurTemp])
 

def printSnowReport(db):
	
	data = db.execute('SELECT * FROM weather').fetchall()
	for obj in data:
		if obj['location'] == 'STP':
			print('Stevens Pass:')

		if obj['location'] == 'CRL':
			print('Crystal Mountain:')

		if obj['location'] == 'MTB':
			print('Mt. Baker:')

		print('Current Forcast: '+ obj['summaryForcast'])
		print('Current Temperature: '+ str(obj['curTemp']))
		print('\n')

		if obj['location'] == 'HOM':
			print('lalala')
	
if __name__== "__main__":
  main()


# #db structure
# CREATE TABLE weather(
# 	id INT NOT NULL,
# 	timeId INT NOT NULL,
# 	latitude VARCHAR(100) NOT NULL,
# 	longitude VARCHAR(100) NOT NULL,
# 	location VARCHAR(100) NOT NULL,
# 	summaryForcast VARCHAR(100) NOT NULL,
# 	curTemp INT NOT NULL,
# );

# **************** Other Notes ***********************
# #Throws erros if any issues in subsequent lines
# set -Eeuo pipefail

# #remove the data base file
# rm -rf database/projjames.sqlite3

# #Sets schema for database
# sqlite3 database/projjames.sqlite3 < sql/schema.sql

# #Puts data in database
# sqlite3 database/projjames.sqlite3 < sql/data.sql




	# value = {
 #   	 "accountWide": True,
 #    	"criteria": [
 #        {
 #            "description": "some description",
 #            "id": 7553,
 #            "max": 1,
 #            "orderIndex": 0
 #        }
 #     ]
 #    }

	# #print(r.json())
	# print(value['accountWide'])
	# print(value['criteria'][0]['max'])
