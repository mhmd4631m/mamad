from django.shortcuts import render
from myapp.models import User
from myapp.forms import newuser
# Create your views here.

def index(b):
    breath = {'my_heart':"I love you"}
    return render(b,'index.html',context=breath)

def user(a):
    form = newuser()
    if a.method == 'POST':
        form = newuser(a.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(a)
        else:
            print('djahj')
    return render(a,'users.html',{'form':form})
