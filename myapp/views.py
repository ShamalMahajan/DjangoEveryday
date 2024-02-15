from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context= {
    'name':'shamal',
    'age': 23,
    'nationality':'indian'
   }
    return render(request,'index.html',context)

def counter(request):
     text = request.GET['text']
     amount_of_words = len(text.split())
     return render(request,'counter.html',{'amount':amount_of_words})
