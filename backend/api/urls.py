from django.urls import path, include
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/node/<int:pk>/", views.NoteDelete.as_view(), name="note-delete"),

]