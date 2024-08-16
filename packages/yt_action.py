import selenium.webdriver
import undetected_chromedriver as uc

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager


class YoutubeActions:
    def __init__(self, profile_directory: str):
        self.profile_directory = profile_directory
        self.is_hide = False
        self.implicitly_wait = 20.0
        self.window_size = (1200, 1200)

    def _make_driver(self) -> uc.Chrome:
        # options = {
        #     # 'proxy': self.proxy
        # }

        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir={self.profile_directory}")

        if self.is_hide:
            options.add_argument("--headless")

        driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(self.implicitly_wait)
        driver.set_window_size(*self.window_size)

        return driver

    def like_the_video(self, link_to_video: str):
        driver = self._make_driver()

        driver.get(link_to_video)

        sleep(5)

        like_button = driver.find_element(By.XPATH, "//like-button-view-model[@class='YtLikeButtonViewModelHost']")
        like_button.click()

        sleep(3)

        driver.quit()

    def subscribe_to_the_channel(self, link_to_video: str):
        driver = self._make_driver()

        driver.get(link_to_video)

        sleep(5)

        subscribe_button = driver.find_element(By.XPATH, "//ytd-subscribe-button-renderer")
        subscribe_button.click()

        sleep(3)

        driver.quit()

    def send_a_comment(self, link_to_video: str, comment: str):
        driver = self._make_driver()

        driver.get(link_to_video)

        sleep(5)

        # driver.execute_script("window.scrollBy(0, 2000);")
        #
        # sleep(2)
        #
        # driver.execute_script("window.scrollBy(0, 500);")
        #
        # sleep(5)
        # button_elements = driver.find_elements(By.XPATH, "//button[@type='button']")

        comment_box = driver.find_element(By.XPATH, "//div[@id='placeholder-area']")
        comment_box.click()

        sleep(1)

        comment_box_2 = driver.find_element(By.XPATH, "//div[@id='contenteditable-root']")
        comment_box_2.click()

        sleep(1)

        comment_box_2.send_keys(comment)

        sleep(1)

        send_button = driver.find_element(By.XPATH, "//ytd-button-renderer[@id='submit-button']")
        send_button.click()

        sleep(5)

        driver.quit()
