from django.shortcuts import render
from django.http import HttpResponse
from requests.exceptions import ConnectionError

import json
import yfinance as yf
import datetime


def home(request):
    return render(request,'ACTUAL/HTML.html')
# Create your views here.
def result(request):
    symbol=request.GET['symbol']
    s = yf.Ticker(symbol)
    output1="That Symbol is not available please enter Valid one"
    output2="No connection please try again later"

    try:
      name=s.info['longName']
    except KeyError:
      return render(request,'ACTUAL/HTML.html',{'output1':output1})
    except IndexError:
      return render(request,'ACTUAL/HTML.html',{'output1':output1})
    except ImportError:
      return render(request,'ACTUAL/HTML.html',{'output1':output1})
    except ConnectionError:  
      return render(request,'ACTUAL/HTML.html',{'output2':output2})  
    name=s.info['longName']
    openprice=s.info['open']
    change=s.info['open']-s.info['previousClose']
    printchange=""
    if(change>0):
      printchange=("+"+str(change))
    else:
      printchange=("-"+str((change*-1)))
    percentagechange=change/s.info['open']  
    printpercentagechange=""
    if(percentagechange>0):
      printpercentagechange=printpercentagechange + ("+"+str(percentagechange)) + '%'
    else:
      printpercentagechange=printpercentagechange + ("-"+str((percentagechange*-1)))  + '%' 
    currentDT = datetime.datetime.now()
    output=['Symbol:', symbol ,'Date',currentDT, 'Name',name,'openprice',openprice, '('+ printchange + ')','('+ printpercentagechange + ')' ]
    return render(request,'ACTUAL/HTML.html',{'outputs':output}) 
