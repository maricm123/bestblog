from django.urls import path
from . import views
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView
app_name = 'blog'

urlpatterns = [
    #post views
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('detail/edit/<int:pk>', UpdatePostView.as_view(), name = 'edit_post'),
    path('detail/<int:pk>/delete', DeletePostView.as_view(), name = 'delete_post'),
]