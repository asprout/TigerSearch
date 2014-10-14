from namefind import getNames
from bs4 import BeautifulSoup
import google
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def check():
    input = request.args.get('question',None)
    if input == None:
        return render_template("TigerSearch.html",list=[])
    else:
        return render_template("TigerSearch.html",list=whoAnswer(input,5))


def whoAnswer(question,n): #returns top n occurrences of names from question
    numPages = 10;#uses top 10 results
    links = google.search("Who " + question,num=numPages,start=0,stop=0,pause=2.0)
    txt = ""
    for i in range(numPages):
        txt += BeautifulSoup(google.get_page(links.next())).getText()
    return getNames(txt,n)

if __name__ == "__main__":
    app.run(debug = "True")

    
