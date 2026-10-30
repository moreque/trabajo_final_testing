import pytest
from pages.registro_page import RegistroPage
from pages.login_page import LoginPage
from pages.turnos_page import TurnosPage

def login_previo(driver):
    reg = RegistroPage(driver)
    reg.open()
    reg.registrar("Usuario Turno", "turno@mail.com", "123456")
    login = LoginPage(driver)
    login.open()
    login.login("turno@mail.com", "123456")

def test_reserva_motivo_limite_100(driver):
    """Detecta el bug en el límite de caracteres (RF-03)."""
    login_previo(driver)
    turnos = TurnosPage(driver)
    motivo_100 = "A" * 100
    turnos.crear_turno("2026-11-10", "10:00", motivo_100)
    assert "Turno reservado correctamente" in turnos.get_flash_message()

def test_acceso_admin_sin_login(driver):
    """Detecta la falta de seguridad en la ruta /admin (RF-06)."""
    driver.get("http://127.0.0.1:5000/admin")
    assert "/login" in driver.current_url