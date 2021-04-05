from django.test import TestCase
from .models import Notes
from django.utils import timezone
import datetime

# Create your tests here.

class CreateNoteTests(TestCase):
    def test_published_recently(self):
        """ to check if a note has been created recently """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_note = Notes(pub_date=time)
        self.assertIs(recent_note.was_published_recently(), True)

    def test_accept_two_notes(self):
        Notes.objects.create(title='1-title', pub_date=timezone.now(), plain_note='1-plain_note')
        Notes.objects.create(title='1-title', pub_date=timezone.now(), plain_note='2-plain_note')
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-title')

