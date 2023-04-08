# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

from os.path import abspath
from time import sleep

services = Service(executable_path=abspath("./geckodriver"))
driver = webdriver.Firefox(service=services)

driver.fullscreen_window()  # esto hace grande la pantalla

# Nos redirecciona a el sitio pasado como argumento al parmetro tal de tipo strgin y una vez abierto nuestro navegador atravz del dirver correspondiente al navegador usado,
driver.get("https://start.garudalinux.org/")
sleep(1)


def init_render(button_redirect: dict) -> None:
    for item_button_redirect in button_redirect:
        path_button_redirect = button_redirect[item_button_redirect]
        clik_redirect_to(
            path_button_redirect=path_button_redirect,
            time_sleep=2,
        )
    else:
        driver.close()


def clik_redirect_to(path_button_redirect: str, time_sleep: int = 3) -> None:
    user_use = driver.find_element(by=By.XPATH, value=path_button_redirect)
    user_use.click()
    sleep(time_sleep)


iter_select_button_redirect = dict(
    path_button_one="/html/body/div/div/div/div/nav/div/div[2]/div[1]/a[1]",
    other_click_download="/html/body/div[2]/span/a[1]",
    other_click_donate="/html/body/div[3]/span/a[4]",
)

init_render(button_redirect=iter_select_button_redirect)



# no se comenta

# input_path = "/html/body/div/div/div/div/nav/div/div[2]/div[2]/div/input"
""" input_use = driver.find_element(by=By.XPATH, value=input_path)

list_letter = "hola mundo"
for item_list_letter in list_letter:
    input_use.send_keys(item_list_letter)
    sleep(1)

sleep(2)
input_use.clear()
sleep(2)

 """


""" p_info_title = "/html/body/div/div/section/div/div/div/div[3]/div[1]/div/a/div/div[1]/div[2]/p[1]"
p_info_text = "/html/body/div/div/section/div/div/div/div[3]/div[1]/div/a/div/div[1]/div[2]/p[2]"

p_scraping_a = driver.find_element(by=By.XPATH, value=p_info_title)
p_scraping_b = driver.find_element(by=By.XPATH, value=p_info_text)

p_scraping_text_a = p_scraping_a.text
p_scraping_text_b = p_scraping_b.text

print("titulo es => ", p_scraping_text_a,
      "\ninformacion es =>", p_scraping_text_b)

 """
""" list_element_Xpath = "/html/body/div/div/section/div/div/div/div[3]/div"
list_web_elemets = driver.find_elements(by=By.XPATH, value=list_element_Xpath)

for item in list_web_elemets:
    text_result = item.text
    print(text_result)
    print('#' * 25)

print(type(list_web_elemets), "=>", len(list_web_elemets))

sleep(2)
driver.close()
 """