from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Notes
from django.views import generic

# Create your views here.
# def index(request):    
    # #New code:
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'NoteKeeper/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Notes.objects.order_by('-pub_date')[:5]