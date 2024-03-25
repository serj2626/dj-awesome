from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from .models import Post, Reply, Tag, Comment
from .forms import PostCreateForm, PostEditForm, CommentCreateForm, ReplyCreateForm
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
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


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PostCreateForm
    template_name = "posts/post_create.html"
    success_message = "Пост успешно создан"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        result = get_data_for_post(post)
        post.author = self.request.user
        post.image = result['image']
        post.title = result['title']
        post.artist = result['artist']
        post.save()
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy('home')
    success_message = "Пост успешно удален"


class PostEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "posts/post_edit.html"
    success_url = reverse_lazy('home')
    success_message = "Пост успешно отредактирован"
    context_object_name = 'post'


class PostDetailView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = CommentCreateForm
    success_message = "Комментарий успешно опубликован"
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_object()
        context['replyform'] = ReplyCreateForm()
        return context

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('post_detail', kwargs={'pk': self.get_object().id})


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


def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    messages.success(request, ' Комментарий успешно удален')
    return redirect('post_detail', pk=comment.post.pk)


def reply_sent(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        replyform = ReplyCreateForm(request.POST)
        if replyform.is_valid():
            reply = replyform.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()
            messages.success(request, ' Ответ успешно опубликован')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def reply_delete(request, pk):
    reply = Reply.objects.get(pk=pk)
    reply.delete()
    messages.success(request, ' Ответ успешно удален')
    return redirect('post_detail', pk=reply.parent_comment.post.pk)


def like_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user != post.author:
        if request.user not in post.likes.all():
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)
    return render(request, 'snippets/likes.html', {'post': post})
