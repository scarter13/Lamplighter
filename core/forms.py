from django import forms
from .models import Company, Contact, Conversation, CompanyNote, ContactNote

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'description',
            'careers',
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'company',
            'email',
            'linkedin',
            'twitter',
            'phone',
            'relationship',
            'status',

        ]

class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = [
            'notes',
        ]

class CompanyNoteForm(forms.ModelForm):
    class Meta:
        model = CompanyNote
        fields = [
            'text',
        ]

class ContactNoteForm(forms.ModelForm):
    class Meta:
        model = ContactNote
        fields = [
            'text',
        ]