import pytest # Importar pytest para la gestión de fixtures
from selenium import webdriver # Importar el webdriver de Selenium
from selenium.webdriver.chrome.options import Options   # Importar opciones de Chrome

@pytest.fixture                                 # Configuración del driver de Selenium
def driver():                                   # Fixture para el driver de Selenium
    options = Options()                         # Configuraciones del navegador
    options.add_argument('--start-maximized')   # Iniciar maximizado
    driver = webdriver.Chrome(options=options)  # Iniciar el navegador Chrome
    driver.implicitly_wait(5)                   # Espera implícita de 5 segundos
    yield driver                                # Proveer el driver a la prueba
    driver.quit()                               # Cerrar el navegador al finalizar la prueba