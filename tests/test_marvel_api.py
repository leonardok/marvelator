from unittest import TestCase

from marvelator.marvel_api import MarvelAPI


class TestMarvelAPI(TestCase):
    def test_get_comic(self):
        api = MarvelAPI()

    def test_get_api_key(self):
        api = MarvelAPI(public_key='dbb1aa9a13b5b3d97c5e9c6363a44d33',
                        private_key='764f276895efb9b5d8c929494e0a99ae540d76b0')
        api.get_comic(10033)
