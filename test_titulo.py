from selenium import webdriver                  #Importamos la librería que permite controlar el navegador
import time                                     #Para hacer pausas visibles (solo demo)

driver = webdriver.Chrome ()                    #Creamos la instancia del driver → abre una ventana de Chrome vacía

try:
    driver.get("https://www.saucedemo.com/")    #Navegamos a la URL de Sauce Demo (pantalla de login)
    print("Titulo:",driver.title)               #Leemos el título de la pestaña → debería salir "Swaq Labs"
    assert driver.title == "Swag Labs"          #Validamos que el título sea el esperado (asegura que cargó bien)
    time.sleep(2)    
    print("✅ Título correcto")
    
except Exception as e:  #Captura cualquier error en el bloque try
    print(f"Error en login: {e}")
    raise   #avisa a pytest que hubo un error#Pausa de 2 s para que lo veas (luego la quitaremos)
finally:
    driver.quit() 