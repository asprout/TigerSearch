import re

def getNames(txt):
    allnames = re.findall('[A-Z][a-z]{2,}(?: [A-Z][a-z]+)?',txt) #gets all capital words/names
    titles = re.findall('(?:Mr. |Ms. |Mrs. |Dr. )[A-Z][a-z]+',txt) #gets all names with a title
    
    g = open("names.csv", 'r')
    doc = g.read()
    g.close()
    namefile = doc.split("\r")[1:]
    
    #gets all the last names that follow the first names
    lastnames = [t.split(' ')[1] for t in allnames if len(t.split(' ')) == 2 and t.split(' ')[0] in namefile]     
    
    #compiles all the names
    found = [n for n in allnames if n.split(' ')[0] in namefile or n in lastnames]   
    
    for z in titles:
        found.append(z)
    
    #tallies up all names
    nameCount = {found.count(w):w for w in found}

    return nameCount

