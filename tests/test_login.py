from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time

def test_login_success(driver):
    print("🔐 Iniciando prueba de login...")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(5)  # Espera para ver el resultado

    assert "/inventory.html" in driver.current_url # Verifica redirección a inventario
    print("✅ Login exitoso → redirigido a /inventory.html")

    title = driver.find_element(By.CLASS_NAME, "title").text # verifica título de la página
    assert title == "Products"
    print("📄 Título de la página:", title)

    driver.save_screenshot("docs/evidencias/login_ok.png")
    