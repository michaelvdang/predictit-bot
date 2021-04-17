# Python program showing the use of
# @property
import requests
from datetime import datetime


class DataCollector:
    def __init__(self):
        self._endpoint = 'https://www.predictit.org/api/marketdata/all/'
        self._response = None

    def collect_data(self):
        self.response = requests.get(self._endpoint)

    def export_content(self):
        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        date_filename = date_string + ".txt"
        full_filepath = "data_logs/" + date_filename

        with open(full_filepath, "w") as text_file:
            print(self.response.content, file=text_file)

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, response):
        self._response = response
