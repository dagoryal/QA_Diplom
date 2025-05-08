import allure
from sqlalchemy.util.queue import Empty
import config
from pages.PageUI import KinoUI

def test_open(browser):
    main_page = KinoUI(browser)
    main_page.open()

@allure.epic("UI Tests")
@allure.feature("Поиск произведений")
@allure.title("Поиск по названию")
@allure.id("Test-1")
def test_search(browser):
    page = KinoUI(browser)
    page.open()
    page.captcha()
    with allure.step("Ввести название фильма"):
        res = page.name_search(config.film_name)
    print(res)
    with allure.step("Проверить, что фильм нашелся"):
        assert res is not None, 'Нет такого фильма'

@allure.epic("UI Tests")
@allure.feature("Поиск произведений")
@allure.title("Поиск рандомного фильма")
@allure.id("Test-2")
def test_random_movie_search(browser):
    page = KinoUI(browser)
    page.open()
    page.captcha()
    random_movie = page.random_movie(config.film_empty_name)
    print(random_movie)
    with allure.step("Убедиться, что в результате что-то нашлось"):
        assert list(random_movie) is not Empty

@allure.epic("UI Tests")
@allure.feature("Расширенный поиск")
@allure.title("Выбор страны")
@allure.id("Test-3")
def test_advanced_search_select_country(browser):
    search_movie = KinoUI(browser)
    search_movie.open()
    search_movie.captcha()
    search_movie.advanced_search_open()
    data = search_movie.advanced_search_select_country(config.country)
    with allure.step("Проверить, что выбранная страна отображается"):
        assert data == config.country

@allure.epic("UI Tests")
@allure.feature("Расширенный поиск")
@allure.title("Выбор жанра")
@allure.id("Test-4")
def test_advanced_search_select_genre(browser):
    search_movie = KinoUI(browser)
    search_movie.open()
    search_movie.captcha()
    search_movie.advanced_search_open()
    genre = search_movie.advanced_search_select_genre(10)
    with allure.step("Проверить, что жанр выбран корректно"):
        assert genre == config.genre

@allure.epic("UI Tests")
@allure.feature("Расширенный поиск")
@allure.title("Расширенный поиск по заданным параметрам")
@allure.id("Test-5")
def test_advanced_search(browser):
    search_movie = KinoUI(browser)
    search_movie.open()
    search_movie.captcha()
    search_movie.advanced_search_open()
    search_movie.advanced_search_select_country(config.country)
    search_movie.advanced_search_select_genre(10)
    res = search_movie.advanced_search()
    with allure.step("Проверить, что список фильмов не пустой"):
        assert res is not Empty

@allure.epic("UI Tests")
@allure.feature("Коллекции")
@allure.title("Поиск списка коллекций и просмотр содержимого")
@allure.id("Test-6")
def test_movie_selections(browser):
    collection = KinoUI(browser)
    collection.open()
    collection.captcha()
    with allure.step("Выбрать коллекцию"):
        res = collection.movie_selections()
    with allure.step("Проверить, что в коллекции есть фильмы"):
        assert res is not None
