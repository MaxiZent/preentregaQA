from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    # Inicializa el navegador
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        
        time.sleep(2)  # Espera para que la página cargue
        
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2)  # Espera para que la página cargue
        
        assert "/inventory.html" in driver.current_url,"No se redirigio al inventario"
        print("Login exitoso y validado")  
    
    except Exception as e:
        print(f"Error en login: {e}")
        raise   #avisa a pytest que hubo un error
    finally:
        driver.quit()