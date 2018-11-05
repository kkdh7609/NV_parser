from bs4 import BeautifulSoup
import urllib


class Parser:
    def __init__(self):
        self.start_url = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime='

    def parsing(self, year, month, day, hour, minute):
        day_string = str(day).zfill(2)
        url_adder = f"{year}-{month}-{day_string}T{hour}%3A{minute}%3A00"
        url = self.start_url + url_adder
        