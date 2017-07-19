from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from upis.models import GJ
from upis.forms import GJForm


class GJList(ListView):
    model = GJ


class CreateGJ(CreateView):
    model = GJ
    form_class = GJForm
    success_url = reverse_lazy('gj_list')


class EditGJ(UpdateView):
    model = GJ
    form_class = GJForm
    success_url = reverse_lazy('gj_list')


class DeleteGJ(DeleteView):
    model = GJ
    success_url = reverse_lazy('gj_list')
