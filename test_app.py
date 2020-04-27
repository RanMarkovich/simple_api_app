import requests
from pytest import fixture


@fixture
def route():
    return 'http://0.0.0.0:5002'


def test_hello_world(route):
    r = requests.get(route)
    assert r.text == 'Hello World!'


def test_hello_name(route):
    name = 'ran'
    r = requests.get(f"{route}/{name}")
    assert r.text == f'Hello {name}!'
