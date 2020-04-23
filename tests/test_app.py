import requests
from pytest import fixture


@fixture
def route():
    return 'http://localhost:5000'


def test_hello_world(route):
    r = requests.get(route)
    assert r.text == 'Hello World!'
