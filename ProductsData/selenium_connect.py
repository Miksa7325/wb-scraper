from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class SeleniumPage():

    def __init__(self):
        options = Options()
        # options.add_argument('--headless=new')
        self.driver = webdriver.Chrome(
            options=options,
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

