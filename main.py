from namefind import getNames
from bs4 import BeautifulSoup
import google

links = google.search("Who led Great Britain during World War 2?",num=1,start=0,stop=0,pause=2.0)

txt = BeautifulSoup(google.get_page(links.next()))
print(getNames(txt.getText(),5))
