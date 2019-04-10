from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import selenium.common.exceptions as sce
import time
import os
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
time1 = time.time()
csv_count = 1804
if os.path.isfile('home\\lsaipc2\\Downloads\\mturk'+str(csv_count)+'.csv'):
    os.remove('home\\lsaipc2\\Downloads\\mturk'+str(csv_count)+'.csv')
rows = []
li = [
        'https://www.linkedin.com/sales/search/people?companyIncluded=Airbnb%3A309694&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Splunk&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Slack%3A1612748&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Square%3A675562&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Affirm%252C%2520Inc.%3A2963249&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Apple%3A162479&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Dropbox%3A167251&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Netflix%3A165158&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=Pinterest%3A1124131&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
        'https://www.linkedin.com/sales/search/people?companyIncluded=SendGrid%3A504748&companyTimeScope=CURRENT&geoIncluded=us%3A0&logHistory=true&logId=2759853986&page=1&searchSessionId=RL2mPxtXSsmiBXlYzqJnLA%3D%3D&titleIncluded=Chief%2520techni%2CChief%2520Executive%2520Officer%3A8%2CChief%2520Marketing%2520Manager%3A19900%2CChief%2520Operating%2520Officer%3A280%2CChief%2520Financial%2520Officer%3A68%2CChief%2520Product%2520Officer%3A11821%2CVice%2520President%3A7%2CFounder%3A35%2CPresident%3A6%2CHead%2520Of%2520Design%3A2024%2CHead%2520Of%2520Sales%3A592%2CHead%2520Of%2520Engineering%3A1945%2CHead%2520Of%2520Products%3A2920%2CChief%2520Architect%3A1149%2CChief%2520Security%2520Officer%3A7960%2CChief%2520Customer%2520Officer%3A26024&titleTimeScope=CURRENT'
]
rows.append(['Company', 'Name','Title', 'Location', 'Url','ImageURL'])
url = 'https://www.linkedin.com/'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
driver.find_element_by_class_name('login-email').send_keys('colleenchien@gmail.com')
driver.find_element_by_class_name('login-password').send_keys('6enji05')
driver.find_element_by_id('login-submit').click()
driver.execute_script("document.body.style_zoom='25%'")
time.sleep(1)
driver.get('https://www.linkedin.com/sales?trk=d_flagship3_nav')
time.sleep(1)

for i in li:

    for j in range(1,41):       #range of pages
        pag = i[0:i.find("page") + 5] + str(j) + i[i.find("page") + 6:]
        print(pag)

        time.sleep(1)
        driver.execute_script("document.body.style_zoom='25%'")
        driver.get(pag)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(750, 1600);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(1550, 2400);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(2350, 3000);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(2950, document.body.scrollHeight);")
        
        text = BeautifulSoup(driver.page_source,'html.parser')
        results = text.find_all('li',attrs={'class':'pv5 ph2 search-results__result-item'})

        if(len(results) < 8):
            break
        for index,each in enumerate(results):
            print(str(j) +"."+ str(index+1))
            try:
                name_path = text.find_all('h4',attrs={'class':'a11y-text'})
                # print(name_path)
                profile = name_path[index*2].getText().split('-')
                # print(profile)
                name = profile[1].strip().encode('utf-8')
                print('name -->' + name)
            except sce.NoSuchElementException as e:
                name = " "
            except IndexError as e:
                name=" "
                
            try:
                designation_path = text.find_all('span',attrs={'class':'Sans-14px-black-75%-bold'})
                # print(designation_path)
                designation = designation_path[index].getText().encode('utf-8')
                print('designation -->' + designation)
            except sce.NoSuchElementException as e:
                designation = " "
            except IndexError as e:
                designation=" "

            company_path = text.find('span',attrs={'class':'result-lockup__position-company'})
            compa = company_path.getText().strip().split()
            company = compa[0].encode('utf-8')
            print("company --> " + str(company))
            
            com_path = text.find_all('span',attrs={'class':'a11y-text'})
            print("Com-path " + str(com_path))
            #name = url_path[index].getText()
            try:
                loc_path = text.find_all('li',attrs={'class':'result-lockup__misc-item'})
                location = loc_path[index].getText().encode('utf-8')
                print('location -->' + location)
            except sce.NoSuchElementException as e:
                location = " "
            except IndexError as e:
                location=" "
            # time.sleep(2)
            try:
                img_path = each.find('img', attrs={'src':re.compile('^(https://media\.licdn\.com/dms/image.+/profile-displayphoto.+)|^(data:image/.+)')})
                #img_path =each.find('img',attrs={'class': 'lazy-image result-lockup__icon loaded'})
                # print(img_path)
                if (img_path is None):
                    img = 'NA'
                else:
                    img = img_path['src'].encode('utf-8')
                # print('img -->' + img)
            except sce.NoSuchElementException as e:
                img = " "
            except TypeError as e:
                img = " "
                
            try:
                url_path = each.find('a', attrs={'href':re.compile('^\/sales.+NAME_SEARCH.+$')})
                # print(url_path)
                try:
                    url = url_path['href'].encode('utf-8')
                    # print(url)
                except sce.NoSuchElementException as e:
                    url = " "
            except sce.NoSuchElementException as e:
                url =" "
            except TypeError as e:
                url = " "
            rows.append([company, name, designation,location , url, img])

            with open('home\\lsaipc2\\Downloads\\mturk'+str(csv_count)+'.csv','w') as f_output:
                try:
                    csv_output = csv.writer(f_output)
                    csv_output.writerows(rows)
                except UnicodeEncodeError as e:
                    print("UnicodeError " + str(e))
                    continue
print(time.time()-time1)










