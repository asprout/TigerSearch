from namefind import getNames
from bs4 import BeautifulSoup
import google

def whoAnswer(question,n): #returns top n occurrences of names from question
    numPages = 10;#uses top 10 results
    links = google.search(question,num=numPages,start=0,stop=0,pause=2.0)
    txt = ""
    for i in range(numPages):
        txt += BeautifulSoup(google.get_page(links.next())).getText()
    return getNames(txt,n)

if __name__ == "__main__":
    print whoAnswer("Who led Great Britain during World War 2?",5)

