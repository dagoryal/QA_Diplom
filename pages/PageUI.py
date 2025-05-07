from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config

class KinoUI:
    def __init__(self, browser: WebDriver) -> None:
        self.url = config.base_url_UI
        self.driver = browser

    def open(self):
        self.driver.get(self.url)

    def name_search(self, name):
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input.kinopoisk-header-search-form-input__input')
        search_input.click()
        search_input.send_keys(name)
        search_input.send_keys(Keys.ENTER)
        try:
            result = self.driver.find_element(By.XPATH, f"//a[text()='{name}']")
        except NoSuchElementException:
            print("Элемент не найден")
            result = None
        return result

    def captcha(self):
        button = self.driver.find_element(By.CSS_SELECTOR, 'div.CheckboxCaptcha-Anchor')
        button.click()

    def random_movie(self, name):
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input.kinopoisk-header-search-form-input__input')
        search_input.click()
        search_input.send_keys(name)
        search_input.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.randomMovieButton")))
        button.click()
        film = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.movieBlock"))).text
        return film

    def advanced_search(self, country):
        movie_search = self.driver.find_element(By.CSS_SELECTOR, 'a.styles_advancedSearch__uwvnd')
        movie_search.click()
        self.driver.find_element(By.ID, 'country')
        wait = WebDriverWait(self.driver, 4)
        selected_country = wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[text()='{country}']")))
        selected_country.click()
        return selected_country.text

    def movie_selections(self):
        self.driver.find_element(By.XPATH,
    '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/nav/ul/li[3]/a').click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.styles_content__2mO6X')))
        lists = self.driver.find_element(By.PARTIAL_LINK_TEXT,'250')
        lists.click()
        movies = self.driver.find_elements(By.CSS_SELECTOR, '.styles_root__ti07r')
        for title in movies:
            return title
