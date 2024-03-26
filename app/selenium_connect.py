from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumPage():

    def __init__(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.driver.quit()

    def process_request(self, url):
        self.driver.get(url)
        counter = 0
        while True:
            cards = self.driver.find_elements(By.XPATH, '//*[@id="route-content"]/div/div[2]/'
                                                        'div[2]/div[2]/div[2]/div')
            if cards:
                break

        for el in cards:
            counter += 1
            if counter % 10 == 0:
                ActionChains(self.driver).move_to_element(el).perform()

        return self.driver.page_source

