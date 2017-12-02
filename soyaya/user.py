import json, os

JSON_DIR = 'volume/users/'

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.json_path = JSON_DIR + 'user{}.json'.format(self.user_id)
        self.data = None  # data not loaded unnecessarily

    def set_me_message(self, new_message):
        self.data['me_message'] = new_message

    def is_registered(self):
        return os.path.isfile(self.json_path)

    def load_data(self):
        with open(self.json_path, 'r') as file:
            self.data = json.loads(file.read())

    def save_data(self):
        with open(self.json_path, 'w') as file:
            file.write(json.dumps(self.data))

    def make_new_user_data(self):
        self.data = {
            'user_id': self.user_id,
            'me_message': 'is da best'
        }
