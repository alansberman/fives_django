from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import GuessForm
def index(request):
    if request.method=='POST':
        form = GuessForm(request.POST)
    
    else:
        form = GuessForm()
    return render(request,'fives/index.html',{'form':form})
# Create your views here.
