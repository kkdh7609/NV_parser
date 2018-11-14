import datetime
import csvmaker

start = datetime.datetime.strptime("2018-11-1", "%Y-%m-%d")
end = datetime.datetime.strptime("2018-11-13", "%Y-%m-%d")
test_csv = csvmaker.CsvMaker("1113.csv", start, end, 2)
test_csv.save_all(30)
