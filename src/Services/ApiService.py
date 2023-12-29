from sys import stderr
import requests
import csv
import os
from datetime import datetime


class ApiService:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com/todos/'
        self.storage_folder = "storage"
        os.makedirs(self.storage_folder, exist_ok=True)

    def run(self):
        print('Running ApiService', file=stderr)

        todos = self.fetch_data()
        self.export_data(todos)

    def fetch_data(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise requests.exceptions.HTTPError("Failed to fetch data")

    def export_data(self, data):
        for d in data:
            self.save_csv(d)
            
    def save_csv(self, data):
        file_name = f"{datetime.now().strftime('%Y_%m_%d')}_{data['id']}.csv"
        file_path = os.path.join(self.storage_folder, file_name)
        with open(file_path, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)