import csv

# file = open("/var/www/env/Data_Gov_Chattisgarh.CSV",'r')
# data= csv.reader(file)
# for row in data:
# 	print(row)
with open("/var/www/env/Data_Gov_Chattisgarh.CSV",  encoding="utf8", errors='ignore') as f:
	data = f.read()
	i = 0
	for row in data.split('\n'):
		if row != '':
			if i > 0:
				cin= row.split(',')[0]
				print(cin.replace("'",'').replace('"',''))

			i +=1

