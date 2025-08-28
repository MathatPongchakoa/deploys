from django.shortcuts import render

def page1(request):
    return render(request, "pages/page1.html")

def page2(request):
    return render(request, "pages/page2.html")

def page3(request):
    return render(request, "pages/page3.html")
