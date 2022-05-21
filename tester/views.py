from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def test(request):
    return render(request,'test1.html')
def test2(request):
    return render(request,'test2.html')
def test3(request):
    return render(request,'test3.html')
def test4(request):
    return render(request,'test4.html')