from django.urls import path


from . import views
from notes.views import CreateAPIView, ListAPIView, UpdateNotesAPIView, RetrieveDestroyAPIView

urlpatterns = [
    path('get_notes/',ListAPIView.as_view(),name="get_notes"),
    path('post_notes/',CreateAPIView.as_view(),name="post_notes"),
    path('delete_notes/<pk>/', RetrieveDestroyAPIView.as_view(), name="delete_note"),
    path('update_notes/<pk>/', UpdateNotesAPIView.as_view(), name="Update_notes"),
    path('retrieve/', views.read_queries, name="retrieve"),
    path('create/', views.create_queries, name="create"),
    path('delete/', views.delete_queries, name="delete"),
    path('update/', views.update_queries, name="update"),
]
