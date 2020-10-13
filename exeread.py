import csv
import os, shutil
from urllib.parse import urljoin, urlparse
import urllib.request
import pymysql, sqlparse
# import xlrd
import openpyxl
from openpyxl import load_workbook

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

filepath="/var/www/seleniumtest/excel/NEW.xlsx"
wb=openpyxl.load_workbook(filepath)
sheet=wb.active
print(sheet)
rowcount = sheet.max_row
colcount = sheet.max_column
print(rowcount)
print(colcount)
for i in  range(1,rowcount,1):
	we =sheet.cell(i,1).value
	try:
		Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(we)+'")')
	except Exception as e:
		print(e)

# with open('/var/www/seleniumtest/excel/eir_April2016.xls', encoding="utf8", errors='ignore') as f:
# # workbook = xlrd.open_workbook("eir_April2016.xls")
# 	# sheet = f.sheet_by_name("New Indian CompniesRgstrd_Apr") 
# 	rowcount = f.nrows
# 	colcount = f.ncols

# 	result_data =[]
# 	for curr_row in range(1, rowcount, 1):
# 	    row_data = []

# 	    for curr_col in range(1, 1, 1):
# 	        # Read the data in the current cell
# 	        data = f.cell_value(curr_row, curr_col)
# 	        print(data)
# 	        row_data.append(data)

# 	    result_data.append(row_data)




# def Query(sql):
# 	db = pymysql.connect("localhost","root","stroops2020","CIN_Number",charset='utf8mb4')
# 	dbc = db.cursor(pymysql.cursors.DictCursor)
# 	output = {}
# 	qcnt = -1
# 	for statement in sqlparse.split(sql):
# 		qcnt = qcnt + 1
# 		dbc.execute(statement)
# 		db.commit()
# 		output[qcnt] = dbc.fetchall()
# 	if qcnt == 0:
# 		output = output[0]
# 	dbc.close()
# 	db.close()
# 	return output


# directory_path = '/var/www/seleniumtest/data'
# destination = '/var/www/seleniumtest/datacom'

# for filename in os.listdir(directory_path):
# 	print(filename)
# 	name1=  directory_path+'/'+ filename
# 	name2 = destination +'/'+ filename

	# file_upload(os.path.join(directory_path, filename))
# with open('/var/www/seleniumtest/excel/eir_April2016.xlsx', encoding="utf8", errors='ignore') as f:
# 	data = f.read()
# 	i = 0
# 	for row in data:
# 		print(row)
		# if row != '':
		# 	if i > 0:
		# 		cin= row.split(',')
		# 		print(cin)
		# 		# ww = cin.replace("'",'').replace('"','')
		# 		# print(ww)
		# 		# try:
		# 		# 	Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
		# 		# except Exception as e:
		# 		# 	print(e)
		
		# i +=1
		# shutil.move(name1, name2) 