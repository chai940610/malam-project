from django.http import HttpResponse
from django.shortcuts import render
import operator

def jason(request):
    return HttpResponse('<h3>Pei Ru<h1>baby<h0>Jasmine')

def bam(request):
    return HttpResponse('Holly')

def mom(request):
    return render(request,'balloon.html',{'BABY':'I LOVE PEI RU'})

def girl(request):
    Bes = request.GET['Jasmine']
    wordlist= Bes.split()
    print(Bes)
    dictionary={}
    for word in wordlist:
        if word in dictionary:
            #increase
            dictionary[word]+=1
        else:  
            #add to the dictionary
            dictionary[word]=1
    sortedword=sorted(dictionary.items(),key=operator.itemgetter(1),reverse=False)

    return render(request,'countone.html',{'Jason': Bes,'x':len(wordlist),'men':dictionary.items(),'apple':sortedword})  

    
def mem(request):
    return render(request,'cb.html')
def son(request):
    return render(request,'sex.html')


