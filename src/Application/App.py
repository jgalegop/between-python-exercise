from src.Services.ApiService import ApiService
import csv
import os
from datetime import datetime

class App:
    def __init__(self):
        self._api_service = ApiService()

    def api_service(self) -> ApiService:
        return self._api_service

    def export_data(self, storage_folder):
        if self._api_service is None or self._api_service.data is None:
            raise Exception("No fetched data to be exported")
        
        # creates folder if there's none
        os.makedirs(storage_folder, exist_ok=True)
        
        for data in self._api_service.data:
            file_name = f"{datetime.now().strftime('%Y_%m_%d')}_{data['id']}.csv"
            file_path = os.path.join(storage_folder, file_name)
            with open(file_path, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)