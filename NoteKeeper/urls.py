from django.urls import path
from . import views
app_name = 'NoteKeeper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.NoteCreate.as_view(), name='create'),
    path('detail/<str:pk>', views.NoteDetailView.as_view(), name='detail'),
    path('update/<str:pk>', views.NoteUpdateView.as_view(), name='update'),
    path('delete/<str:pk>/', views.NoteDeleteView.as_view(), name='delete'),
]