from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('blog:detail', args=(str(self.id)))
        # If we are reversing inside a function we can use reverse().
        return reverse('blog:home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('blog:detail', args=(str(self.id)))
        # If we are reversing inside a function we can use reverse().
        return reverse('blog:home')
