import allure
import requests
import config

class KinoAPI:

    def __init__(self, url: config.base_url_api, token: config.main_token):
        self.base_url = url
        self.headers = {
            "accept": "application/json",
            "X-API-KEY": token,
            "Content-Type": "application/json"
        }

    @allure.step("Поиск произведения по названию")
    def name_search(self, query: str):
        url = f"{self.base_url}/movie/search?page=1&limit=10&query={query}"
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    @allure.step("Поиск произведения по {film_id}")
    def id_search(self, film_id: int):
        url = f"{self.base_url}/movie/{film_id}"
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    @allure.step("Поиск рандомного фильма {kino_type} с рейтингом {imdb} >7")
    def random_film(self, kino_type: int, imdb: str):
        url = f"{self.base_url}/movie/random?notNullFields=name&tipe={kino_type}&rating.imdb={imdb}"
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    @allure.step('Поиск Российских фильмов из коллекции {lists}')
    def top_rus_films(self, country_name: str, lists: str):
        url = f"{self.base_url}/movie?page=1&limit=250&countries.name={country_name}&lists={lists}"
        resp = requests.get(url, headers=self.headers)
        return resp.json()

    @allure.step("Поиск методом POST")
    def post_request(self, query: str, body):
        url = f"{self.base_url}/movie/search?page=1&limit=10&query={query}"
        resp = requests.post(url, headers=self.headers, json=body)
        return resp.json()

    @allure.step("Установить лимит элементов на странице {limit}")
    def zero_limit(self, query: str, limit: int):
        url = f"{self.base_url}/movie/search?page=1&limit={limit}&query={query}"
        resp = requests.get(url, headers=self.headers)
        return resp.json()
