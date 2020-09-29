from django.shortcuts import render,HttpResponse
import json
import re
from django.http import JsonResponse

# Create your views here.

#CASE CONVERTER

def caseConverter(request):
    return render(request,'Text/caseConverter.html')

def count(request):
    t=json.loads(request.body)
    char_count=len(t["text"])
    word_count=len(t["text"].split())
    line_count=t["text"].split("\n")
    if line_count==['']:
        line_count=0
    else:
        line_count=len(line_count)
    return JsonResponse({"char_count":char_count,"word_count":word_count,"line_count":line_count})


def upperCase(request):
    t=json.loads(request.body)
    return JsonResponse({"upperCase":t["text"].upper()})


def lowerCase(request):
    t=json.loads(request.body)
    return JsonResponse({"lowerCase":t["text"].lower()})


def sentanceCase(request):
    t=json.loads(request.body)
    t["text"]=t["text"].lower()
    t["text"]=t["text"].split(".")
    sen=[]
    for i in t["text"]:
        for j in i:
            if j.isalpha():
                i=i.replace(j,j.upper(),1)
                sen.append(i)
                break
    return JsonResponse({"sentanceCase":".".join(sen)})

def titleCase(request):
    t=json.loads(request.body)
    return JsonResponse({"titleCase":t["text"].title()})


def swapCase(request):
    t=json.loads(request.body)
    return JsonResponse({"swapCase":t["text"].swapcase()})


def camelCase(request):
    t=json.loads(request.body)
    t["text"]=t["text"].title()
    t["text"]=t["text"].split()
    t["text"][0]=t["text"][0].lower()
    return JsonResponse({"camelCase":"".join(t["text"])})


def snakeCase(request):
    t=json.loads(request.body)
    t["text"]=t["text"].lower()
    t["text"] = t["text"].split()
    return JsonResponse({"snakeCase":"_".join(t["text"])})



def kebabCase(request):
    t=json.loads(request.body)
    t["text"] = t["text"].lower()
    t["text"] = t["text"].split()
    return JsonResponse({"kebabCase": "-".join(t["text"])})


def pascalCase(request):
    t=json.loads(request.body)
    t["text"] = t["text"].title()
    t["text"] = t["text"].split()
    return JsonResponse({"pascalCase": "".join(t["text"])})


def upperSnakeCase(request):
    t=json.loads(request.body)
    t["text"]=t["text"].title()
    t["text"] = t["text"].split()
    return JsonResponse({"upperSnakeCase":"_".join(t["text"])})

def download(request):
    t = json.loads(request.body)
    response = HttpResponse(t["text"],content_type="application/msword")
    return response

#ASCII TEXT CONVERTER

def asciiConverter(request):
    return render(request,'Text/asciiText.html')

def asciiConversion(request):
    t = json.loads(request.body)
    if t["option"]=="Text to ASCII Converter":
        t["text"]=[str(ord(i)) for i in t["text"]]
        t["text"]=" ".join(t["text"])
    else:
        try:
            t["text"]=[chr(int(i)) for i in t["text"].split()]
            t["text"] = "".join(t["text"])
        except:
            return JsonResponse({"Error": "Please Enter Valid ASCII Value, Each Separated By A Space."})
    return JsonResponse({"asciiConversion": t["text"]})


#Binary TEXT CONVERTER

def binaryConverter(request):
    return render(request,'Text/binaryText.html')

def binaryConversion(request):
    t = json.loads(request.body)
    if t["option"]=="Text to Binary Numbers Converter":
        t["text"]=[format(ord(i), 'b') for i in t["text"]]
        t["text"]=" ".join(t["text"])
    else:
        try:
            t["text"]=[chr(int(i,2)) for i in t["text"].split()]
            t["text"] = "".join(t["text"])
        except:
            return JsonResponse({"Error": "Please Enter Valid Binary Numbers, Each Separated By A Space."})
    return JsonResponse({"binaryConversion": t["text"]})


#OCTAL TEXT CONVERTER

def octalConverter(request):
    return render(request,'Text/octalText.html')

def octalConversion(request):
    t = json.loads(request.body)
    if t["option"]=="Text to Octal Converter":
        t["text"]=[format(ord(i), 'o') for i in t["text"]]
        t["text"]=" ".join(t["text"])
    else:
        try:
            t["text"]=[chr(int(i,8)) for i in t["text"].split()]
            t["text"] = "".join(t["text"])
        except:
            return JsonResponse({"Error": "Please Enter Valid Octal Numbers, Each Separated By A Space."})
    return JsonResponse({"octalConversion": t["text"]})


#HexaDecimal TEXT CONVERTER

def hexConverter(request):
    return render(request,'Text/hexText.html')

def hexConversion(request):
    t = json.loads(request.body)
    if t["option"]=="Text to Hexadecimal Converter":
        t["text"]=[format(ord(i), 'x') for i in t["text"]]
        t["text"]=" ".join(t["text"])
    else:
        try:
            t["text"]=[chr(int(i,16)) for i in t["text"].split()]
            t["text"] = "".join(t["text"])
        except:
            return JsonResponse({"Error": "Please Enter Valid Hexadecimal Numbers, Each Separated By A Space."})
    return JsonResponse({"hexConversion": t["text"]})


#Word Occurrence Counter

def wordOccurrence(request):
    return render(request,'Text/wordOccurrence.html')

def wordOccurrenceCounter(request):
    t = json.loads(request.body)
    word_occurrence=dict()
    t["text"]=t["text"].lower().strip()
    t["text"]=re.sub(r'[,\./?!]'," ",t["text"])
    for word in t["text"].split():
        if word!='':
            word_occurrence[word]=word_occurrence.get(word,0)+1
    l=[]
    for word,count in word_occurrence.items():
        l.append((count,word))
    l.sort(reverse=True)
    text=''
    if t["option"]=="All":
        n=len(l)
    else:
        n=int(t["option"][len(t["option"])-3:len(t["option"])])
    for i,j in l[:n]:
        text+=j.capitalize()+" : "+str(i)+"\n"
    return JsonResponse({"wordOccurrenceCounter": text})


#Extract Email From Text

def extractEmail(request):
    return render(request, 'Text/extractEmail.html')

def emailExtractor(request):
    t = json.loads(request.body)
    emails=re.findall(r'[\w\-\._]+@[\w\-\._]+\.[a-z]+',t["text"])
    if emails==[]:
        return JsonResponse({"emailExtractor": "NO EMAILS FOUND."})
    emails='\n'.join(emails)
    return JsonResponse({"emailExtractor": emails})


#Extract URLS From Text

def extractUrl(request):
    return render(request, 'Text/extractUrl.html')

def urlExtractor(request):
    t = json.loads(request.body)
    urls=re.findall(r'((?:https?://)?www\..*?(?:\.\S+)*\.[a-z]+|https?://(?:www\.)?.*?(?:\.\S+)*\.[a-z]+)',t["text"])
    if urls==[]:
        return JsonResponse({"urlExtractor": "NO URLS FOUND."})
    urls='\n'.join(urls)
    return JsonResponse({"urlExtractor": urls})


#Extract Phone Numbers From Text

def extractPhoneno(request):
    return render(request, 'Text/extractPhoneno.html')

def phonenoExtractor(request):
    t = json.loads(request.body)
    phoneno=re.findall(r'((?:(?:\+?91|0|\d{3})[ -]?)?(?:\d{3}[ -\.]?\d{3}[ -\.]?\d{4}|\d{5}[ -\.]?\d{5}|\d{4}[ -\.]?\d{4}|\(\d{3}\)[ -\.]?\d{3}[ -\.]?\d{4}|\d{3}[ -\.]?\d{5}|\d{2}[ -\.]?\d{3}[ -\.]?\d{3}))',t["text"])
    if phoneno==[]:
        return JsonResponse({"phonenoExtractor": "NO PHONE NUMBERS FOUND."})
    phoneno='\n'.join(phoneno)
    return JsonResponse({"phonenoExtractor": phoneno})


#Find Subtext From Text

def findSubText(request):
    return render(request, 'Text/findSubText.html')

def subTextFinder(request):
    t = json.loads(request.body)
    t["text"]=re.sub("<","&lt;",t["text"])
    t["text"] = re.sub(">", "&gt;", t["text"])
    t["find"]=re.sub("<","&lt;",t["find"])
    t["find"] = re.sub(">", "&gt;", t["find"])
    sub=re.findall(t["find"],t["text"])
    if sub==[]:
        return JsonResponse({"sub_found": "NO MATCH FOUND"})
    t["text"]=re.sub('{}'.format(t["find"]),"<span class='sub-found'>{}</span>".format(t["find"]),t["text"])
    return JsonResponse({"sub_found":t["text"]})


#Replace Subtext From Text

def replaceSubText(request):
    return render(request, 'Text/replaceSubText.html')

def subTextReplacer(request):
    t = json.loads(request.body)
    t["text"] = re.sub("<", "&lt;", t["text"])
    t["text"] = re.sub(">", "&gt;", t["text"])
    t["find"] = re.sub("<", "&lt;", t["find"])
    t["find"] = re.sub(">", "&gt;", t["find"])
    t["replace"] = re.sub("<", "&lt;", t["replace"])
    t["replace"] = re.sub(">", "&gt;", t["replace"])
    sub = re.findall(t["find"], t["text"])
    if sub == []:
        return JsonResponse({"sub_found": "NO MATCH FOUND"})
    t["text"] = re.sub('{}'.format(t["find"]), "<span class='sub-found'>{}</span>".format(t["replace"]), t["text"])
    return JsonResponse({"sub_found": t["text"]})