# Python App Exercise

## Exercise
- Use the ApiService to fetch TODOs from an API and save them into the _storage_ folder
    - TODOs can be accessed from this URL: https://jsonplaceholder.typicode.com/todos/
    - Each TODO should be saved on a single file in CSV format
    - The filename must contain the TODO "id" prefixed with the current date.
        - Example: 2021_04_28_123.csv


## Extra points
- Use _requests_ library from [PyPI](https://pypi.org/project/requests/)


## Comments on exercise
- Added requests to library
- Tried to separate functionalities between App and ApiService
    - ApiService just fetches data
    - App does the rest of the export
    - On main.py different things can be done in case the App class would ever have more functionality
