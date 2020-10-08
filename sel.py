from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time 
import csv
from selenium.webdriver.chrome.options import Options


prefs = {"download.default_directory" : '/var/www/env'}

options = Options()			
options.add_argument("--start-maximized")
# options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("prefs",prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")

browser = webdriver.Chrome('/var/www/chromedriver', options=options)



browser.get('https://data.gov.in/catalog/company-master-data?filters%5Bfield_catalog_reference%5D=354261&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc')
# browser.maximize_window()
csvfile = browser.find_element_by_class_name("csv")
action = ActionChains(browser);

action.move_to_element(csvfile).click().perform()
time.sleep(2)

selector1 = browser.find_element_by_id("edit-download-reasons-1")
action.move_to_element(selector1).click().perform()
time.sleep(1)

selector2 = browser.find_element_by_id("edit-reasons-d-4")
browser.execute_script("arguments[0].click();", selector2)

nameinput= browser.find_element_by_id("edit-name-d")
nameinput.send_keys('luhegytti')

mailinput = browser.find_element_by_id("edit-mail-d")
mailinput.send_keys('luhegytti-0826@yopmail.com')

submitinput = browser.find_element_by_id("edit-submit")
submitinput.click()


# reader = csv.DictReader(open("Data_Gov_Chattisgarh.csv"))
# for raw in reader:
#     print(raw)

with open("/var/www/seleniumtest/data/Data_Gov_Chattisgarh.CSV",  encoding="utf8", errors='ignore') as f:
	data = f.read()
	i = 0
	for row in data.split('\n'):
		if row != '':
			if i > 0:
				cin= row.split(',')[0]
				print(cin.replace("'",'').replace('"',''))

			i +=1
# browser.quit()