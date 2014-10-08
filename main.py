from namefind import getNames
from bs4 import BeautifulSoup
import google

links = google.search("Who is the current principal of Stuyvesant High School?",num=1,start=0,stop=0,pause=2.0)

txt = BeautifulSoup(google.get_page(links.next()))
print(getNames(txt.getText()))
