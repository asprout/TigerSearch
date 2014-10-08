import re

month1 = open("months.csv",'r').read().strip()
months = month1.split("\n")

test = "Jan 14, 2014"

def vali_date(d):
    matches = re.findall('([A-Za-z]|\d{0,2})+[,/ ] *\d{1, 2}[,/ ] *d{0, 4}', d)
    print matches

if __name__=="__main__":
    vali_date(test)
