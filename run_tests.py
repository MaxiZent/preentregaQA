import pytest

test_files = [ # Lista de archivos de prueba a ejecutar
    "tests/test_login.py",
    "tests/test_inventario.py",
    "tests/test_carrito.py",
]

# Argumento para ejecutar pytest con los archivos de prueba especificados
pytest_args = test_files + ["-v", "--html=reports/report.html", "--self-contained-html"] # Genera un reporte HTML

pytest.main(pytest_args) # Ejecuta pytest con los argumentos proporcionados