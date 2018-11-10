import csv
import datetime
import parse_rank


class CsvMaker:
    def __init__(self, path, start_date, end_date):
        self.path = path
        self.date_list = [start_date + datetime.timedelta(days=x) for x in range(0, (end_date - start_date).days)]

    def save_all(self, min_term):                  # (60 % min_term) should be 0
        ps = parse_rank.Parser()
        with open(self.path, 'w', encoding='euc-kr', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for date in self.date_list:
                year = date.year
                month = date.month
                day = date.day
                for i in range(0, 24):
                    for j in range(0, 60, min_term):
                        comb_time = f"{year}-{month}-{day} {i}:{j}"
                        writer.writerow([comb_time])
                        self.save_one(ps, writer, year, month, day, i, j)

    def save_one(self, ps, wr, year, month, day, hour, minute, transpose=False):
        rank_list = ps.parsing(year, month, day, hour, minute)
        if transpose:
            rank_list = [list(x) for x in zip(*rank_list)]        # transpose the rank_list
        for rank in rank_list:
            print(rank)
            wr.writerow(rank)
        


if __name__ == "__main__":
    start = datetime.datetime.strptime("2018-10-14", "%Y-%m-%d")
    end = datetime.datetime.strptime("2018-10-31", "%Y-%m-%d")
    test_csv = CsvMaker("abc2.csv", start, end)
    test_csv.save_all(30)
