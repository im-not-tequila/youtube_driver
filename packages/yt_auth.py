import undetected_chromedriver as uc

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager


class YoutubeAuthorization:
    def __init__(self, login: str, password: str, profiles_directory: str):
        self.login = login
        self.password = password
        # self.proxy = proxy
        self.is_hide = False
        self.profiles_directory = profiles_directory
        self.implicitly_wait = 20.0
        self.window_size = (800, 1200)

    def _make_driver(self) -> uc.Chrome:
        # options = {
        #     # 'proxy': self.proxy
        # }
        profile_directory = f'{self.profiles_directory}/{self.login}'

        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir={profile_directory}")

        if self.is_hide:
            options.add_argument("--headless")

        driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(self.implicitly_wait)
        driver.set_window_size(*self.window_size)

        return driver

    def auth(self) -> str:
        driver = self._make_driver()

        _auth_link = 'https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https://www' \
                     '.youtube.com/signin?action_handle_signin=true&app=desktop&hl=ru&next=https%3A%2F%2Fwww.youtube.com' \
                     '%2F%3FthemeRefresh%3D1&hl=ru '

        driver.get(_auth_link)

        sleep(3)

        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        email_input.send_keys(self.login)
        sleep(3)
        button_elements = driver.find_elements(By.XPATH, "//button[@type='button']")

        for button_element in button_elements:
            if 'Далее' in button_element.text:
                button_element.click()

        sleep(5)
        password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

        sleep(10)

        driver.quit()

        return f'{self.profiles_directory}/{self.login}'

    def check_yt_authorization(self) -> bool:
        driver = self._make_driver()

        driver.get("https://www.youtube.com")

        sleep(5)

        try:
            driver.find_element(By.XPATH, '//a[@aria-label="Войти"]')
            return False
        except NoSuchElementException:
            return True

