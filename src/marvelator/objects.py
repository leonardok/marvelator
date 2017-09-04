class Character:
    def __init__(self):
        pass


class Comic:
    def __init__(self):
        # The story's description
        self.description = None

        # A list of names and pictures of the characters that features in the story
        self.features = []

        # The Marvel attribution text
        self.marvel_text = None

    def load_from_json(self, comic_data):
        self.marvel_text = comic_data.get('title')
        self.description = comic_data.get('description')
        self.features = comic_data.get('characters')
