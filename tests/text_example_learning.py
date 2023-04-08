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
    user_use.click()  # se usara 3 veces x cada redireccion de la pagina
    sleep(time_sleep)  # espera que la pagina cargue


iter_select_button_redirect = dict(
    path_button_one="/html/body/div/div/div/div/nav/div/div[2]/div[1]/a[1]",
    other_click_download="/html/body/div[2]/span/a[1]",
    other_click_donate="/html/body/div[3]/span/a[4]",
)

init_render(button_redirect=iter_select_button_redirect)
