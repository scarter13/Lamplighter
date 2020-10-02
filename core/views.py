from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Company, Contact, Conversation, CompanyNote, ContactNote
from .forms import CompanyForm, ContactForm, ConversationForm, CompanyNoteForm, ContactNoteForm

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

def add_company(request):
    if request.method == "POST":
        form = CompanyForm(data=request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect(to='my_companies')
    else:
        form = CompanyForm()

    return render(request, "lamp/add_company.html", {"form": form})

def my_contacts(request):
    contacts = request.user.contacts.all()
    return render(request, "lamp/my_contacts.html", {"contacts": contacts})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect(to='my_contacts')
    else:
        form = ContactForm()

    return render(request, "lamp/add_contact.html", {"form": form})

"""
@login_required
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to='my_qbox')
    else:
        form = QuestionForm()

    return render(request, "qbox/create_question.html", {"form": form})
"""