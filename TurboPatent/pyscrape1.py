from selenium import webdriver
import csv
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as sce
import time
import os
import pandas as pd

time1 = time.time()
if os.path.isfile('/home/lsaipc3/Downloads/res_new33.xlsx'):
    os.remove('/home/lsaipc3/Downloads/res_new33.xlsx')
rows = []
c= -1
rows.append(['Publication Number','Antecedent Basis Comments', 'Figure reference comments', 'Claim support comments','Claim order comments','101 Elligibility'])
path = '/home/lsaipc3/Downloads/input33.xlsx'
df = pd.read_excel(path)
li = df['app_num'].apply(str)
url = 'https://trials.turbopatent.us/signin/?next=/roboreview/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element_by_name('username').send_keys('pbhushan@scu.edu')
driver.find_element_by_name('password').send_keys('6D466xFHzr')
driver.find_element_by_tag_name('button').click()
driver.execute_script("document.body.style.zoom='zoom %'")
time.sleep(2)
for i in range(len(li)-1):
    print(li[i])
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@name='appNum']").send_keys(li[i])
    #print(BeautifulSoup(driver.page_source,'html.parser'))
    print("keys Done")
    driver.find_element_by_tag_name('button').click()
    try:
        print("in try " + li[i])
        WebDriverWait(driver, 90).until(                           #implicit wait
            EC.presence_of_element_located((By.CLASS_NAME, "ui-report-page-print-footer-text"))
        )
    except sce.NoSuchElementException as e:
        print("No Such Element Found" + li[i])
        driver.get('https://trials.turbopatent.us/roboreview/')
        c+=1
        continue

    except sce.TimeoutException as e:
        print ("TimeOut Exception" + li[i])
        driver.get('https://trials.turbopatent.us/roboreview/')
        c+=1
        continue
    text = BeautifulSoup(driver.page_source,'html.parser')
    tab = text.find_all('div',attrs={'class':'ui-report-claimset-markup-header-item-count js-report-claimset-markup-header-item-count'})
    antecedent = tab[0].getText().strip()
    fig = tab[1].getText().strip()
    claim = tab[2].getText().strip()
    forma = tab[3].getText().strip()
    #print(antecedent)
    #print(fig)
    #print(claim)
    #print(forma)
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath("//a[@class='ui-report-alice-score-show-hide-btn js-alice-show-hide-btn']").click()
        alice = driver.find_element_by_xpath("//div[@class='ui-report-caret-box js-caret']")
        al = alice.get_attribute('style')
        alice_per = al.split(' ')[1]
    except:
        print("no slide button detail for " + li[i]);
        alice_per = 'NA'
    #print(alice_per)
    rows.append([li[i],antecedent,fig,claim,forma,alice_per])
    print(time.time() - time1)                      #prints the total time taken
    c+=1
    with open('/home/lsaipc3/Downloads/res_new33.xlsx','w',newline='') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerows(rows)
    if c == len(li) -1:
        break
    else:
        driver.back()

