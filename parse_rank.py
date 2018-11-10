from bs4 import BeautifulSoup
import urllib.request
import ssl


class Parser:
    def __init__(self):
        self.start_url = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime='
        self.opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_TLSv1)))
        self.opener.addheaders = [('User-agent', 'Whale/1.3.53.4')]
        urllib.request.install_opener(self.opener)

    def parsing(self, year, month, day, hour, minute):
        day_string = str(day).zfill(2)
        hour_string = str(hour).zfill(2)
        min_string = str(minute).zfill(2)
        url_adder = f"{year}-{month}-{day_string}T{hour_string}%3A{min_string}%3A00"
        url = self.start_url + url_adder
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        rank_list = soup.find_all('div', {'class': 'keyword_rank'})
        parse_list = []
        for ranks in rank_list:
            cat_list = []
            for rank in ranks.find_all('li'):
                cat_list.append(rank.span.string)
            parse_list.append(cat_list)
        return parse_list


if __name__ == "__main__":
    p = Parser()
    print(p.parsing(2018, 11, 5, 0, 0))           # just for testing
