from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectListView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:pk>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectListView.as_view(), name='user-project-list'),
]
