from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from newsletters.forms import ClientForm
from newsletters.models import Client

def index(request):
    # Testing
    return render(request, 'newsletters/base.html')


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletters:client_list')
