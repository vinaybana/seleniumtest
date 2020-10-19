from queue import *
from threading import Thread
import os	
import csv																																																																																																																																																																																		
import pymysql, sqlparse

concurrent = 100
que = Queue(concurrent*100)

def Query(sql):
	db = pymysql.connect("localhost","root","stroops2020","CIN_Number",charset='utf8mb4')
	dbc = db.cursor(pymysql.cursors.DictCursor)
	output = {}
	qcnt = -1
	for statement in sqlparse.split(sql):
		qcnt = qcnt + 1
		dbc.execute(statement)
		db.commit()
		output[qcnt] = dbc.fetchall()
	if qcnt == 0:
		output = output[0]
	dbc.close()
	db.close()
	return output

def DataProcess():
	while True:
		param = que.get()
		cin = param['cin']
		print("processing....", cin)
		try:
			Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(cin)+'")')
		except Exception as e:
			print(e)

		que.task_done()

# directory_path = '/var/www/seleniumtest/data4'
# destination = '/var/www/seleniumtest/datacom'


for i in range(concurrent):
	t = Thread(target=DataProcess)
	t.daemon = True
	t.start()

# for filename in os.listdir(directory_path):
# 	name1=  directory_path+'/'+ filename
# 	name2 = destination +'/'+ filename

with open("/var/www/seleniumtest/data4/company.csv", encoding="utf8", errors='ignore') as f:
	data = csv.reader(f)
	for row in data:
		param = {'cin':row[1]}
		que.put(param)

que.join()
	# print(data)

# for q in query:
	
# 	i = 0
# 	for row in data.split('\n'):
# 		if row != '':
# 			if i > 0:
# 				cin= row.split(',')[1]
# 				print(cin)
# 				ww = cin.replace("'",'').replace('"','')
# 				print(ww)
# 				param = {'cin':ww}
# 				que.put(param)

# 		i +=1
# 	shutil.move(name1, name2)


	# ipid = str(q['id'])
	# ipnum = str(q['number'])
	# param = {'ipid':ipid, 'ipnum':ipnum,}
	# que.put(param)




