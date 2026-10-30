from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:5000/login"

    def open(self):
        self.driver.get(self.url)

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 5)
        
        email_elem = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_elem.clear()
        email_elem.send_keys(email)

        pass_elem = self.driver.find_element(By.NAME, "password")
        pass_elem.clear()
        pass_elem.send_keys(password)

        submit = self.driver.find_element(By.XPATH, "//input[@type='submit'] | //button[@type='submit'] | //button")
        submit.click()