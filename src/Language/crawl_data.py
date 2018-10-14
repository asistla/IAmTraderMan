import csv
import datetime

def getCsv(csvfile):
    with open(csvfile) as f:
        lines=f.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].strip().split(',')
    return lines
    
#def 