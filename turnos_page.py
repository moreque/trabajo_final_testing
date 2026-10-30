from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TurnosPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:5000/turnos"

    def open(self):
        self.driver.get(self.url)

    def crear_turno(self, fecha, hora, motivo, duracion="30"):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "fecha"))).send_keys(fecha)
        self.driver.find_element(By.NAME, "hora").send_keys(hora)
        
        dur = self.driver.find_element(By.NAME, "duracion")
        dur.clear()
        dur.send_keys(duracion)
        
        mot = self.driver.find_element(By.NAME, "motivo")
        mot.clear()
        mot.send_keys(motivo)
        
        submit = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@action='/turnos/nuevo']//button | //form[@action='/turnos/nuevo']//input[@type='submit']")
        ))
        submit.click()

    def get_flash_message(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flash"))).text

    def contar_turnos_tabla(self):
        return len(self.driver.find_elements(By.XPATH, "//table//tr[td]"))