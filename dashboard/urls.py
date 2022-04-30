from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('notes', views.notes, name="notes"),
    path('delete_note/<int:pk>', views.delete_note, name="delete-note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes-detail"),
    
    path('youtube', views.youtube, name="youtube"),

    path('books', views.books, name="books"),

    path('dictionary', views.dictionary, name="dictionary"),

    path('wiki', views.wiki, name="wiki"),

]