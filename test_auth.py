import sys
import os
import pytest

# Asegura que Python encuentre la carpeta 'pages' agregando la raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.registro_page import RegistroPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("nombre, email, password", [
    ("", "test@mail.com", "123456"),
    ("Juan", "", "123456"),
    ("Juan", "test@mail.com", ""),
])
def test_registro_campos_vacios(driver, nombre, email, password):
    reg = RegistroPage(driver)
    reg.open()
    reg.registrar(nombre, email, password)
    assert reg.es_campo_invalido_html5() or "Completá todos los campos" in reg.get_flash_message()

def test_login_correcto(driver):
    reg = RegistroPage(driver)
    reg.open()
    reg.registrar("Tester", "tester@mail.com", "123456")
    
    login = LoginPage(driver)
    login.login("tester@mail.com", "123456")
    assert "/turnos" in driver.current_url
    