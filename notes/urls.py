from django.urls import path
from django.http import request
from .views import (
    home_view,
    NotesView,
    note_detail,
    create_note,
    SignUpView,
    delete_note,
    LoginView,
                    )

app_name = 'notes'

urlpatterns = [
    path('', home_view, name='home'),
    path('notes/', NotesView.as_view(), name='notes-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('notes/add/', create_note, name='note-add'),
    path('notes/<pk>/', note_detail, name='notes-detail'),
    path('notes/delete/<pk>/', delete_note, name='delete-note'),
    path('signup/', SignUpView.as_view(), name='sign-up'),
]
