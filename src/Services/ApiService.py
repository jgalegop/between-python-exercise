from sys import stderr
import requests

class ApiService:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/todos/'

    def run(self):
        print('Running ApiService', file=stderr)

        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise requests.exceptions.HTTPError("Failed to fetch data")
