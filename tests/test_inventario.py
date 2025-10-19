import time
from selenium.webdriver.common.by import By

def test_inventory_elements(driver):
    print("📦 Iniciando prueba de inventario...")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    assert "Swag Labs" in driver.title
    print("✅ Título de la página OK")

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"🛍️ Se encontraron {len(productos)} productos.")
    assert len(productos) > 0

    primero = productos[0]
    nombre = primero.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primero.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"🧾 Primer producto: {nombre} - Precio: {precio}")

    driver.save_screenshot("docs/evidencias/inventario_ok.png")