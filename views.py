from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
class HomePageView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'all_post_list'
# Create your views here.
