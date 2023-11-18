from django.http import HttpResponse
from django.shortcuts import render
# def aboutus(request):
#     return HttpResponse("welcome my site")

# def coursedetails(request,courseid):
#     return HttpResponse(courseid)

def homepage(request):
    return render(request,"index.html")