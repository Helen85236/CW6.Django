from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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

    # Basic validation using models fields
    def form_valid(self, form):
        return super().form_valid(form)



class ClientDetailView(DetailView):
    model = Client

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('newsletters:client_update', args=[self.object.pk])

    # Basic validation using models fields
    def form_valid(self, form):
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('newsletters:client_list')
