from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def sf(request):
    sfo=Studentform()
    d={'sfo':sfo}
    if request.method=='POST':
        sfd=Studentform(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
        else:
          return HttpResponse('invalid data')
    return render(request,'sf.html',d)