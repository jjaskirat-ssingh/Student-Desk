from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    
    path('notes', views.notes, name="notes"),
    path('delete_note/<int:pk>', views.delete_note, name="delete-note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes-detail"),
    path('ref_detail/<int:pk>', views.ReferencesDetailView.as_view(), name="ref-detail"),
    
    path('youtube', views.youtube, name="youtube"),

    path('refer', views.references, name="refer"),

    path('books', views.books, name="books"),

    path('dictionary', views.dictionary, name="dictionary"),

    path('wiki', views.wiki, name="wiki"),
]
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)