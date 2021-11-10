from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact

class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact

class ContactCreate(CreateView):
    model = Contact
    fields =['name','email','address','phone']
    template_name = "contacts/contact_form.html"
    success_url = "/"

class ContactUpdate(UpdateView):
    model = Contact
    fields =['name','email','address','phone']
    success_url = "/"

class ContactDelete(DeleteView):
    model = Contact
    success_url = "/"


