from django.shortcuts import render
from django.http import JsonResponse

import json
import time

def convertTime(t): # http://strftime.org/
    epoch = time.gmtime(t) #t/1e6
    GMT=time.strftime('%A, %b %d, %Y', epoch)
    return GMT

# required for get requests that dont rely on static
def getQuora2(request):
	#Get/open json:
    data = open('home/Quora.json')
    data1 = json.load(data)  # deserialises it
    data.close()

    #reformat: I'll re do organization in program later
    data2 = data1.copy()
    for k,v in data1.items():
        if type(v["answer"]) == dict:
            # Sends aepoch to outer dict for easier sorting
            del data2[k]["qepoch"]
            data2[k]["epoch"] = data2[k]["answer"].pop("aepoch")//1e6
            data2[k]["link"] = data2[k]["answer"].pop("alink")
        else:
            # rename for sorting
            data2[k]["epoch"] = data2[k].pop("qepoch") #*1e6
            data2[k]["link"] = data2[k].pop("qlink")
        data2[k]["time"] = convertTime(data2[k]["epoch"])
        data2[k]["show"] = False
    return JsonResponse(data2)
