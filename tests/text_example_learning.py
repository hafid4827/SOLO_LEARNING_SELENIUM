# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


from os.path import abspath
from time import sleep

services = Service(executable_path=abspath("./geckodriver"))
driver = webdriver.Firefox(service=services)

driver.fullscreen_window()  # esto hace grande la pantalla

# busca en el buscador por defecto de neustro navegador
driver.get("https://start.garudalinux.org/")
sleep(1)

path_button_one = "/html/body/div/div/div/div/nav/div/div[2]/div[1]/a[1]"
user_use = driver.find_element(by=By.XPATH, value=path_button_one)
sleep(1)

user_use.click() # se usara 3 veces x cada redireccion de la pagina
sleep(5)

driver.close()