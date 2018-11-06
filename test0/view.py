from django.http import HttpResponse
from django.shortcuts import render
import operator as op

def homepage( request ):
    return render( request , 'home.html')


def reto(request):
    return render(request,'reto.html')

def count( request ):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    #print("The browser has --> " + fulltext)

    dictionarycount = {}

    for word in wordlist:

        if word in dictionarycount:
            dictionarycount[word] += 1

        else:
            dictionarycount[word] = 1


    wordsorted = sorted(dictionarycount.items() , key=op.itemgetter(1) , reverse=True )

    
    return render( request , 'count.html' , {'fulltext':fulltext , 'count':len(wordlist) , 'dictionarycount':wordsorted } )

"""
def marco( request ):
    return HttpResponse( '<h1>The best programmer ever!</h1>')

def hello( request ):
    return HttpResponse('This is the beginning of my empire!')

def homepage2( request ):
    return render( request , 'home.html',{'test':'pass information from python'} )
"""
