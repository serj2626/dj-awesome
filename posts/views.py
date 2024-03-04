from django.shortcuts import redirect, render
from .models import Post
from .forms import PostCreateForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup
from .service import get_data_for_post



class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"


def home_view(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context=context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        result = get_data_for_post(post)

        post.image = result['image']
        post.title = result['title']
        post.artist = result['artist']

        post.save()
        return super().form_valid(form)
