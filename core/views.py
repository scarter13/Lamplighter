from django.shortcuts import render, redirect
from django.db.models import Count

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        #return redirect (to = 'my_home')
        return render(request, "lamp/my_lamp.html")
    return render(request, "lamp/home.html")

def my_home(request):
    return render(request, "lamp/my_lamp.html")

def my_companies(request):
    companies = request.user.companies.all()
    #think about a helper function to sort them.  Javascript?
    #companies = lamp_sort(companies)
    #companies = companies.annotate(num_contacts=Count("contacts"))
    return render(request, "lamp/my_companies.html", {"companies": companies})