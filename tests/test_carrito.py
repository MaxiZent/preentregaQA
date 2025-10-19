import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_cart(driver):
    print("🛒 Iniciando prueba de carrito...")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()
    print("➕ Producto añadido al carrito")

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"
    print("✅ Badge del carrito muestra:", badge)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    print("🧾 Producto en carrito:", producto_en_carrito)
    assert producto_en_carrito != ""

    time.sleep(3)
    driver.save_screenshot("docs/evidencias/carrito_ok.png")