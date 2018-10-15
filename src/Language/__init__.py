from Language.crawl_data import getCsv, crawl
import csv
import datetime
csvData = getCsv("E:\\hist.csv")
htmldata=crawl()
print htmldata