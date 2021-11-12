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

# Formulario de Google
URL_GOOGLE_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSe3eW2zH2nUIIovvmH565mlPAZdH8nJyJLm6dgGaiBTUc3t6A/viewform'

dictionary1 = config()
dictionary2 = gsheets()
dictionary1.update(dictionary2)
print(f'Data:\n{dictionary1}\n')

class GoogleForms(unittest.TestCase):

    
    def setUp(self):  
        # Prepara el entorno de la prueba
        # https://chromedriver.chromium.org/downloads 
        # You must download the chromedriver compatible with your browser
        self.driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver')
        driver = self.driver
        driver.get(URL_GOOGLE_FORM)
        driver.maximize_window()
        


    def test_filling_data(self):
        # automatizacion
        driver = self.driver
        # selectores xpath - encontramos los campos donde insertaremos la data
        #title = driver.find_element_by_css_selector('div.freebirdFormviewerViewHeaderTitle')
        #print(f'hola {title.text}')
        #titulo = driver.find_element_by_class_name('freebirdFormviewerViewHeaderTitle')
        #print(titulo.text)
        #names = driver.find_element_by_css_selector('div.quantumWizTextinputPapertextareaMainContent div.quantumWizTextinputPapertextareaContentArea textarea#quantumWizTextinputPapertextareaInput')
        #/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input
        #prueba = driver.find_element_by_class_name('quantumWizTextinputPapertextareaInput')
        #//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea
        names = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ids = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        email = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        team_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        yesterday = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        today = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        impediments = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        #//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span
        # insertamos la data almacenada en el diccionario en el campo correspondiente.
        names.send_keys(dictionary1['names'])
        # Hacemos una pausa de 1 seg. para ver la informacion que se agrega.
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

        #submit_button.click()  # BOTON DE ENVIAR !!!
        # ***Descomenta la linea anterior para que se envie el formulario***
        
        time.sleep(30)
        # Esperamos unos segundos antes de cerrar la ventana del navegador.
    
    
    def tearDown(self):
        #cerrar navegador
        self.driver.quit()

if __name__ == "__main__":

    # se corre el test
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='', report_name='autofillingoogleforms'))
    # se crea un reporte html