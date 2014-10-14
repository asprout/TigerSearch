import re

#returns top n names by number of occurrences in an ordered list of tuples
def getNames(txt, num):
    allnames = re.findall('[A-Z][a-z]{2,}(?: [A-Z][a-z]+)?',txt) #gets all capital words/names
    titles = re.findall('(?:Mr. |Ms. |Mrs. |Dr. )[A-Z][a-z]+',txt) #gets all names with a title
    
    g = open("names.csv", 'r')
    doc = g.read()
    g.close()
    namefile = doc.split("\r")[1:]
    
    #gets all the last names that follow the first names
    lastnames = {t.split(' ')[1]:t.split(' ')[0] for t in allnames if len(t.split(' ')) == 2 and t.split(' ')[0] in namefile}     
    
    #compiles all the names
    found = [n for n in allnames if n.split(' ')[0] in namefile or n in lastnames.keys()]

    #converts found last names to their respective full names
    for n in range(len(found)):
        if found[n] in lastnames.keys():
             found[n] = lastnames[found[n]] + ' ' + found[n]
    
    for z in titles:
        found.append(z)
    
    #tallies up all names
    nameCount = {w:found.count(w) for w in found}
    nameCount = [(w,str(nameCount[w])) for w in nameCount.keys()]
    nameCount.sort(key = lambda x: int(x[1]),reverse = True)

    return nameCount[:num]

