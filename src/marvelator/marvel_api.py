import time
from hashlib import md5

import requests

from marvelator.objects import Comic


class MarvelAPI:
    def __init__(self, public_key, private_key):
        self.api_prefix = 'https://gateway.marvel.com/v1/public/'

        self.public_key = public_key
        self.private_key = private_key

    def get_from_marvel(self, url, additional_params=None):
        """
        Get data from the Marvel servers

        :param url: the endpoint url
        :param additional_params: additional params for the GET request
        :return: the request result
        """
        ts = str(int(time.time()))

        params = {
            'ts': ts,
            'apikey': self.public_key,
            'hash': md5(ts + self.private_key + self.public_key).hexdigest(),
        }

        # if additional params were passed, update the default params
        if additional_params is not None:
            params.update(additional_params)

        return requests.get(url, params)

    def get_comic(self, comic_id):
        """
        Get a comic details

        :param comic_id: comic id
        :return: a Comic instance
        """
        api_url = self.api_prefix + 'comics/' + str(comic_id)
        response = self.get_from_marvel(api_url)

        response_json = response.json()
        comic_data = response_json.get('data').get('results')[0]

        comic = Comic()
        comic.load_from_json(comic_data)

        return comic

    def get_character_comics(self, character_id):
        """
        Get a list of all character comics.
        For now it returns only a vector of IDs, but it can be extended.

        :param character_id: character is
        :return: a list of comic ids
        """
        limit = 100
        count = 100
        offset = 0

        comics_id_list = []

        while count == limit:
            api_url = self.api_prefix + 'characters/' + str(character_id) + '/comics'
            response = self.get_from_marvel(api_url, {'limit': limit, 'offset': offset})

            response_json = response.json()

            count = response_json.get('data').get('count')
            offset += count

            comics_id_list += [comic.get('id') for comic in response_json.get('data').get('results')]

        return comics_id_list
