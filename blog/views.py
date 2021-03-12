from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
# def home(request):
#     return render(request, 'home.html', {})
from .form import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-date']

class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'body')
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    # If we are using success_url we have to use reverse_lazy().
    success_url = reverse_lazy('blog:home')

class AddCategoryView(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'add_category.html'
    # fields = ('title', 'body')
    # fields = '__all__'