from django.urls import path


from . import views
from notes.views import CreateAPIView, ListAPIView, UpdateNotesAPIView, RetrieveDestroyAPIView

urlpatterns = [
    path('get_notes/',ListAPIView.as_view(),name="get_notes"),
    path('post_notes/',CreateAPIView.as_view(),name="post_notes"),
    path('delete_notes/<pk>/', RetrieveDestroyAPIView.as_view(), name="delete_note"),
    path('update_notes/<pk>/', UpdateNotesAPIView.as_view(), name="Update_notes"),
    path('get/',views.note_get_view, name="notes"),
]