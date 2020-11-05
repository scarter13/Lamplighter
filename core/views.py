from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Company, Contact, Conversation, CompanyNote, ContactNote
from .forms import CompanyForm, CompanyContactForm, ContactForm, ConversationForm, CompanyNoteForm, ContactNoteForm


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

def add_company_note(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    if request.method == "POST":
        form = CompanyNoteForm(data=request.POST)
        if form.is_valid():
            company_note = form.save(commit=False)
            company_note.user = request.user
            company_note.company = company
            company_note.save()
            return redirect(to='company_detail', company_pk=company.pk)
    else:
        form = CompanyNoteForm()

    return render(request, "lamp/add_company_note.html", {"company": company, "form": form})

def company_note_detail(request, note_pk):
    note = get_object_or_404(CompanyNote, pk=note_pk)
    company = note.company
    return render(request, "lamp/company_note_detail.html", {"note": note, "company": company})

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

def add_company_contact(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    if request.method == "POST":
        form = CompanyContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.company = company
            contact.save()
            return redirect(to='company_detail', company_pk=company.pk)
    else:
        form = CompanyContactForm()

    return render(request, "lamp/add_company_contact.html", {"form": form, "company": company})

def delete_contact(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    conversations = contact.conversations.all()[:3]
    if request.method == 'POST':
        contact.delete()
        return redirect(to='my_contacts')

    return render(request, "lamp/delete_contact.html",
                  {'contact': contact, 'conversations': conversations})

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

""" You might consider removing contact_notes from the context in the contact_detail below; All you need at this point is the num_notes since you are no longer trying to render notes on the detail page.
"""
def contact_detail(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    conversations = contact.conversations.all()[:3]
    contact_notes = contact.notes.all()
    num_notes = len(contact_notes)
    return render(request, "lamp/contact_detail.html", {"contact": contact, "conversations": conversations, "contact_notes": contact_notes, "num_notes": num_notes})

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

    return render(request, "lamp/add_contact_note.html", {"contact": contact, "form": form})

def contact_notes(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    notes = contact.notes.all()
    #context = {
    #    'contact': contact,
    #    'notes': notes,
    #}
    return render(request, "lamp/contact_notes.html", {"contact": contact, "notes": notes})

def contact_note_detail(request, note_pk):
    note = get_object_or_404(ContactNote, pk=note_pk)
    contact = note.contact
    return render(request, "lamp/contact_note_detail.html", {"note": note, "contact": contact})

def edit_note(request, note_pk):
    note = get_object_or_404(request.user.contact_notes, pk=note_pk)
    contact = note.contact
    if request.method == 'POST':
        form = ContactNoteForm(data=request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect(to='contact_notes', contact_pk=contact.pk)
    else:
        form = ContactNoteForm(instance=note)
    return render (request, "lamp/edit_note.html", {"form": form, "note": note})   

def delete_note(request, note_pk):
    note = get_object_or_404(ContactNote, pk=note_pk)
    contact = note.contact
    if request.method == 'POST':
        note.delete()
        all_notes = contact.notes.all()
        if len(all_notes) == 0:
            return redirect(to='contact_detail', contact_pk=contact.pk)
        return redirect(to='contact_notes', contact_pk=contact.pk)

    return render(request, "lamp/delete_note.html",
                  {"note": note, 'contact': contact})

def add_conversation(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    if request.method == "POST":
        form = ConversationForm(data=request.POST)
        if form.is_valid():
            conversation = form.save(commit=False)
            conversation.user = request.user
            conversation.contact = contact
            conversation.save()
            return redirect(to='contact_detail', contact_pk=contact.pk)
    else:
        form = ConversationForm()

    return render(request, "lamp/add_conversation.html", {"contact": contact, "form": form})

def conversation_detail(request, conversation_pk):
    conversation = get_object_or_404(Conversation, pk=conversation_pk)
    contact = conversation.contact
    return render(request, "lamp/conversation_detail.html", {"conversation": conversation, "contact": contact})

def edit_conversation(request, conversation_pk):
    conversation = get_object_or_404(Conversation, pk=conversation_pk)
    if request.method == 'POST':
        form = ConversationForm(data=request.POST, instance=conversation)
        if form.is_valid():
            conversation = form.save()
            return redirect(to='conversation_detail', conversation_pk=conversation.pk)
    else:
        form = ConversationForm(instance=conversation)
    return render (request, "lamp/edit_conversation.html", {"form": form, "conversation": conversation})    

def delete_conversation(request, conversation_pk):
    conversation = get_object_or_404(Conversation, pk=conversation_pk)
    contact = conversation.contact
    if request.method == 'POST':
        conversation.delete()
        all_conversations = contact.conversations.all()
        if len(all_conversations) == 0:
            return redirect(to='contact_detail', contact_pk=contact.pk)
        return redirect(to='conversations', contact_pk=contact.pk)

    return render(request, "lamp/delete_conversation.html",
                  {"conversation": conversation, 'contact': contact})

def conversations(request, contact_pk):
    contact = get_object_or_404(Contact, pk=contact_pk)
    conversations = contact.conversations.all()
    return render(request, "lamp/conversations.html", {'contact': contact, 'conversations': conversations})
