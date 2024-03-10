from django.shortcuts import redirect, render
from .models import Post, Tag
from .forms import PostCreateForm, PostEditForm
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
from .service import get_data_for_post
from django.views.generic.edit import DeleteView, UpdateView
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"


class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "posts/post_create.html"
    success_message = "Пост успешно создан"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        result = get_data_for_post(post)

        post.image = result['image']
        post.title = result['title']
        post.artist = result['artist']

        post.save()
        return super().form_valid(form)


class PostDelete(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy('home')
    success_message = "Пост успешно удален"


class PostEditView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "posts/post_edit.html"
    success_url = reverse_lazy('home')
    success_message = "Пост успешно отредактирован"
    context_object_name = 'post'


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


def page_not_found(request, exception):
    return render(request, '404.html')


class CategoryView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = Tag.objects.get(slug=self.kwargs.get('slug'))
        return context
