from sqlalchemy.util.queue import Empty

import config
from pages.PageUI import KinoUI

def test_open(browser):
    main_page = KinoUI(browser)
    main_page.open()

def test_search(browser):
    page = KinoUI(browser)
    page.open()
    page.captcha()
    res = page.name_search(config.film_name)
    print(res)
    assert res is not None, 'Нет такого фильма'

def test_empty_search(browser):
    page = KinoUI(browser)
    page.open()
    page.captcha()
    random_movie = page.random_movie(config.film_empty_name)
    print(random_movie)
    assert list(random_movie) is not Empty

def test_advanced_search(browser):
    search_movie = KinoUI(browser)
    search_movie.open()
    search_movie.captcha()
    data = search_movie.advanced_search(config.country)
    assert data == config.country

def test_movie_selections(browser):
    collection = KinoUI(browser)
    collection.open()
    collection.captcha()
    res = collection.movie_selections()
    assert res is not None
