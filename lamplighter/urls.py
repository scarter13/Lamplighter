"""lamplighter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('', core_views.login, name= 'login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('lamp/companies/', core_views.my_companies, name = 'my_companies'),
    path('lamp/company/<int:company_pk>/', core_views.company_detail, name = 'company_detail'),
    path('lamp/contacts/', core_views.my_contacts, name = 'my_contacts'),
    path('lamp/contact/<int:contact_pk>/', core_views.contact_detail, name = 'contact_detail'),
    path('lamp/contact/edit/<int:contact_pk>/', core_views.edit_contact, name = 'edit_contact'),
    path('lamp/contact/note/<int:note_pk>/', core_views.contact_note_detail, name = 'contact_note_detail'),
    path('lamp/contact/notes/<int:contact_pk>', core_views.contact_notes, name = 'contact_notes'),
    path('lamp/conversation/<int:conversation_pk>', core_views.conversation_detail, name = 'conversation_detail'),
    path('lamp/conversation/new/<int:contact_pk>', core_views.add_conversation, name = 'add_conversation'),
    path('lamp/conversation/edit/<int:conversation_pk>', core_views.edit_conversation, name = 'edit_conversation'),
    path('lamp/note/delete/<int:note_pk>', core_views.delete_note, name = 'delete_note'),
    path('lamp/note/edit/<int:note_pk>', core_views.edit_note, name = 'edit_note'),
    path('lamp/add/company/', core_views.add_company, name = 'add_company'),
    path('lamp/add/contact/', core_views.add_contact, name = 'add_contact'),
    path('lamp/add/contact/note/<int:contact_pk>/', core_views.add_contact_note, name='add_contact_note'),
 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
