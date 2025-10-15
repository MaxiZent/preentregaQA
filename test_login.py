from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome ()
driver.implicitly_wait (5)

try:
    #LOGIN
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user") #ingresamos usuario
    driver.find_element(By.ID, "password").send_keys("secret_sauce")    #ingresamos contraseña
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(2)  #Pausa para ver lo que sucede (solo demo)
    
    # VALIDACIÓN: Verifica que el usuario fue redirigido al inventario
    assert "inventory.html" in driver.current_url, "Login fallido o redirección incorrecta" # Verifica que la URL contiene 'inventory.html'
    print("✅ Login exitoso")
    
except Exception as e:  #Captura cualquier error en el bloque try
    print(f"Error en login: {e}")
    raise   #avisa a pytest que hubo un error
    
finally:
    driver.quit() #Cierre limpio: mata la sesión y la ventana