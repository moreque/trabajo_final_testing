from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistroPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:5000/registro"

    def open(self):
        self.driver.get(self.url)

    def registrar(self, nombre, email, password):
        wait = WebDriverWait(self.driver, 5)
        
        nom_elem = wait.until(EC.presence_of_element_located((By.NAME, "nombre")))
        nom_elem.clear()
        if nombre:
            nom_elem.send_keys(nombre)

        email_elem = self.driver.find_element(By.NAME, "email")
        email_elem.clear()
        if email:
            email_elem.send_keys(email)

        pass_elem = self.driver.find_element(By.NAME, "password")
        pass_elem.clear()
        if password:
            pass_elem.send_keys(password)

        submit = self.driver.find_element(By.XPATH, "//input[@type='submit'] | //button[@type='submit'] | //button")
        submit.click()

    def get_flash_message(self):
        try:
            wait = WebDriverWait(self.driver, 3)
            return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flash"))).text
        except Exception:
            return ""

    def es_campo_invalido_html5(self):
        """Devuelve True si la validación HTML5 del navegador detuvo el envío por campos requeridos."""
        return self.driver.execute_script(
            "return document.querySelector('form').checkValidity() === false;"
        )