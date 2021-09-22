'''
    Miguel Sánchez
    @miguelsanchezco

'''

import time
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from modules.config import config
from modules.gsheets import gsheets


dictionary1 = config()
dictionary2 = gsheets()
dictionary1.update(dictionary2)

print(f'Data:\n{dictionary1}\n')

class GoogleForms(unittest.TestCase):

    
    def setUp(self):  # self - cls
        # Prepara el entorno de la prueba
        # https://chromedriver.chromium.org/downloads 
        # You must download the chromedriver compatible with your browser
        self.driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver')
        driver = self.driver
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSd8XQoio5u2W1y70CcGPdW_5uGlgtADAH82DzfcNDfSUjy3aQ/viewform')
        driver.maximize_window()
        

    def test_filling_data(self):
        # automatizacion
        # selectores xpath
        driver = self.driver
        names = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
        ids = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
        email = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        team_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        yesterday = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        today = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        impediments = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        
        names.send_keys(dictionary1['names'])
        time.sleep(1)
        ids.send_keys(dictionary1['ids']) 
        time.sleep(1)
        email.send_keys(dictionary1['email'])
        time.sleep(1)
        team_name.send_keys(dictionary1['team_name'])
        time.sleep(1)
        yesterday.send_keys(dictionary1['yesterday'])
        time.sleep(1)
        today.send_keys(dictionary1['today'])
        time.sleep(1)
        impediments.send_keys(dictionary1['impediments']) 
        time.sleep(1)
        submit_button.click()
        time.sleep(30)
    

    
    def tearDown(self):
        #cerrar navegador
        self.driver.quit()

if __name__ == "__main__":

    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='', report_name='autofillingoogleforms'))
