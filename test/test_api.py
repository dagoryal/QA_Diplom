import config
from pages.PageAPI import KinoAPI
import allure

api = KinoAPI(config.base_url_api, config.main_token)

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.title("Поиск по валидному имени")
@allure.story("Поиск произведения по названию")
@allure.id("Test-1")
def test_name_search():
    kino = api.name_search(query=config.query_valid)
    kino_total = kino["docs"]['names' == config.query_valid]
    print(len(kino_total))
    with allure.step("Проверить, что длина списка найденных фильмов >0"):
        assert len(kino_total) > 0

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск произведения по id")
@allure.title("Поиск по валидному id")
@allure.id("Test-2")
def test_id_search():
    film = api.id_search(film_id=config.id_valid)
    film_name = film['name']
    print(film_name)
    with allure.step("Проверить, что название фильма соответствует"):
        assert film_name == "Тайна Коко"

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск рандомного произведения")
@allure.title("Поиск рандомного произведения с рейтингом imdb>7")
@allure.id("Test-3")
def test_random_film():
    movie = api.random_film(kino_type=config.type_kino, imdb=config.imdb)
    name_movie = movie['name']
    print(name_movie)
    with allure.step("Проверить, что список не пустой"):
        assert len(name_movie) > 0

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск коллекций произведений")
@allure.title("Поиск Российских фильмов из коллекции Топ 250")
@allure.id("Test-4")
def test_list_films():
    top_film = api.top_rus_films(country_name=config.countries, lists=config.lists)
    list_films = top_film['docs']
    film_names = [item['name'] for item in list_films]
    print(list(film_names))
    with allure.step("Проверить, что длина списка найденных фильмов >0"):
        assert len(film_names) > 0

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск произведения по названию")
@allure.title("Поиск по невалидному названию")
@allure.id("Test-5")
def test_non_existent_name_search():
    kino = api.name_search(query=config.non_existent_name)
    kino_total = kino["total"]
    with allure.step("Проверить, что с некорректным названием фильмов нет"):
        assert kino_total == 0

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск произведения по id")
@allure.title("Поиск по невалидному id")
@allure.id("Test-6")
def test_invalid_id_search():
    film = api.id_search(film_id=config.id_invalid)['message']
    with allure.step("Проверить, что по невалидному id невозможно отправить запрос"):
        assert film == ['Значение поля id должно быть в диапазоне от 250 до 10000000!']

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск методом POST")
@allure.title("Поиск методом POST")
@allure.id("Test-7")
def test_post_request():
    kino = api.post_request(query='thor', body="")
    status = kino['statusCode']
    message = kino['message']
    with allure.step("Проверить статус код"):
        assert status == 404
    with allure.step("Убедиться, что метод POST не работает"):
        assert message == 'Cannot POST /v1.4/movie/search?page=1&limit=10&query=thor'

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Поиск произведения без токена")
@allure.title("Отправить запрос без токена")
@allure.id("Test-8")
def test_no_token():
    kino = KinoAPI(config.base_url_api, '').name_search(query=config.query_valid)
    message = kino['message']
    status = kino['statusCode']
    with allure.step("Проверить, что без токена нельзя отправлять запрос"):
        assert message == 'В запросе не указан токен!'
    with allure.step("Проверить статус код"):
        assert status == 401

@allure.epic("API Tests")
@allure.feature("Поиск произведений")
@allure.story("Установить лимит элементов на странице 0")
@allure.title("Отправить запрос с лимитом элементов на странице = 0")
@allure.id("Test-9")
def test_zero_limit():
    kino = api.zero_limit(query=config.query_valid, limit=0)
    message = kino['message']
    status = kino['statusCode']
    with allure.step("Проверить, что количество элементов на странице min 1"):
        assert message == ['limit must not be less than 1']
    with allure.step("Проверить статус код"):
        assert status == 400
