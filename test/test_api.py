import config
from pages.PageAPI import KinoAPI

api = KinoAPI(config.base_url_api, config.main_token)

def test_name_search():
    kino = api.name_search(query=config.query_valid)
    kino_total = kino["docs"]['names' == config.query_valid]
    print(len(kino_total))
    assert len(kino_total) > 0

def test_id_search():
    film = api.id_search(film_id=config.id_valid)
    film_name = film['name']
    print(film_name)
    assert film_name == "Тайна Коко"

def test_random_film():
    movie = api.random_film(kino_type=config.type_kino, imdb=config.imdb)
    name_movie = movie['name']
    print(name_movie)
    assert len(name_movie) > 0

def test_list_films():
    top_film = api.top_rus_films(country_name=config.countries, lists=config.lists)
    list_films = top_film['docs']
    film_names = [item['name'] for item in list_films]
    print(list(film_names))
    assert len(film_names) > 0

def test_non_existent_name_search():
    kino = api.name_search(query=config.non_existent_name)
    kino_total = kino["total"]
    assert kino_total == 0

def test_invalid_id_search():
    film = api.id_search(film_id=config.id_invalid)['message']
    assert film == ['Значение поля id должно быть в диапазоне от 250 до 10000000!']

def test_post_request():
    kino = api.post_request(query='thor', body="")
    status = kino['statusCode']
    message = kino['message']
    assert status == 404
    assert message == 'Cannot POST /v1.4/movie/search?page=1&limit=10&query=thor'

def test_no_token():
    kino = KinoAPI(config.base_url_api, '').name_search(query=config.query_valid)
    message = kino['message']
    status = kino['statusCode']
    assert message == 'В запросе не указан токен!'
    assert status == 401

def test_zero_limit():
    kino = api.zero_limit(query=config.query_valid, limit=0)
    message = kino['message']
    status = kino['statusCode']
    assert message == ['limit must not be less than 1']
    assert status == 400

# def test_incorrect_url():
#     search = api.incorrect_url(query=config.query_valid)
#     message = search['message']
#     assert message