# Preentrega Proyecto SauceDemo

Este proyecto automatiza pruebas funcionales sobre la web saucedemo.com, incluyendo:
- ✅ Login exitoso
- ✅ Verificación del catálogo
- ✅ Interacción con productos y carrito

🛠 Tecnologías usadas
- Python
- Selenium
- Pytest
- pytest-html (para generar reportes en HTML)
- ChromeDriver

📦 Instalación de dependencias
Primero, asegurate de tener Python instalado. Luego, podés instalar las dependencias con:
pip install selenium pytest pytest-html


O si tenés un archivo requirements.txt, simplemente:
pip install -r requirements.txt


▶️ Cómo correr los tests
Desde la raíz del proyecto, ejecutá:
pytest -v --html=reporte.html


## Estructura
preentrega-maxicenturion/
├── tests/                  # Pruebas automatizadas 
├── docs/                   # Evidencias y reporte HTML 
├── evidencias/             # Capturas de pantalla 
└── reporte.html            # Reporte de ejecución
├── conftest.py             # Fixture para Selenium
├── selectors.md            # Documentación de selectores
├── requirements.txt        # Dependencias
