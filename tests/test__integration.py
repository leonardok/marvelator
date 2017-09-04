from unittest import TestCase

import os

from marvelator.marvel_api import MarvelAPI


class TestIntegrations(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestIntegrations, self).__init__(*args, **kwargs)

        self.private_key = os.environ.get('MARVEL_PRIV_KEY')
        self.public_key = os.environ.get('MARVEL_PUB_KEY')

    def test_get_comic(self):
        api = MarvelAPI(public_key=self.public_key, private_key=self.private_key)
        api.get_comic(10033)

    def test_get_comics_of_char(self):
        api = MarvelAPI(public_key=self.public_key, private_key=self.private_key)
        result = api.get_character_comics(1009282)

        self.assertGreater(len(result), 1)
