from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Notes
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'NoteKeeper/index.html'
    context_object_name = 'NoteList'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Notes.objects.order_by('-pub_date')[:5]

class NoteCreate(generic.CreateView):
    model = Notes
    fields = ['title', 'content']
    template_name = 'NoteKeeper/notekeeper_add.html'
    success_url ="/"

class NoteDetailView(generic.DetailView):
    model = Notes
    template_name = 'NoteKeeper/notekeeper_detail.html'

class NoteUpdateView(generic.UpdateView):
    model = Notes
    fields = ['title', 'content']
    template_name = 'NoteKeeper/notes_form_update.html'
    mod_date = timezone.now()
    success_url ="/"

class NoteDeleteView(generic.DeleteView):
    model = Notes
    success_url ="/"
        
    

