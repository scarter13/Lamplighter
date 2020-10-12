from django.shortcuts import render, redirect, get_object_or_404
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
    print("inside my companies view")
    #think about a helper function to sort them.  Javascript?
    #companies = lamp_sort(companies)
    companies = companies.annotate(num_contacts=Count("contacts"))
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

def company_detail(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    contacts = company.contacts.all()
    company_notes = company.notes.all()
    return render(request, "lamp/company_detail.html", {"company": company, "contacts": contacts, "company_notes": company_notes})

def my_contacts(request):
    print("navigated to my contacts")
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

def edit_contact(request, contact_pk):
    contact = get_object_or_404(request.user.contacts, pk=contact_pk)
    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect(to='contact_detail', contact_pk=contact.pk)
    else:
        form = ContactForm(instance=contact)


    return render (request, "lamp/edit_contact.html", {"form": form, "contact": contact})

def contact_detail(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    conversations = contact.conversations.all()
    contact_notes = contact.notes.all()
    return render(request, "lamp/contact_detail.html", {"contact": contact, "conversations": conversations, "contact_notes": contact_notes})

def add_contact_note(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    if request.method == "POST":
        form = ContactNoteForm(data=request.POST)
        if form.is_valid():
            contact_note = form.save(commit=False)
            contact_note.user = request.user
            contact_note.contact = contact
            contact_note.save()
            return redirect(to='contact_detail', contact_pk=contact.pk)
    else:
        form = ContactNoteForm()

    return render(request, "lamp/add_contactNote.html", {"contact": contact, "form": form})
    
"""
def create_answer(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect(to='show_question', question_pk=question.pk)
    else:
        form = AnswerForm()

    return render(request, "qbox/create_answer.html", {"form": form, "question": question})
"""