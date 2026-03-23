import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()                         # Configuración de opciones del navegador
    options.add_argument('--start-maximized')   # Inicia el navegador maximizado

    driver = webdriver.Chrome(options=options)  # Inicia el driver de Chrome
    driver.implicitly_wait(5)                   # Espera implícita de 5 segundos

    yield driver                                # Proporciona el driver a la prueba
    driver.quit()                               # Cierra el navegador al finalizar