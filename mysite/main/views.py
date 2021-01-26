from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PostCreateForm, CommentForm
from django.contrib import messages
from django.conf import settings
from .models import Post, Comment
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
import os


# Create your views here.

def LikeView(response, pk):
    post = get_object_or_404(Post, id=response.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=response.user.id).exists():
        post.likes.remove(response.user)
        liked = False
    else:
        post.likes.add(response.user)
        liked = True
    return HttpResponseRedirect(reverse('post-view', args=[str(pk)]))

def home(response):
    if response.method == "POST":
        search = response.POST.get("search")
        print(search)
        return redirect("search-results", search=search)
    context = {"posts": Post.objects.all().order_by("-date_posted")}
    return render(response, "main/main.html", context)

def search_results(response, search):
    if Post.objects.filter(title__icontains=search):
        search_results = Post.objects.filter(title__icontains=search).order_by("-date_posted")
    else:
        raise Http404("No results Found.")
    for post in Post.objects.all():
        post = post
    context = {"search_results": search_results, "post": post, "search":search}
    return render(response, "main/search_results.html", context)

def post_view(response, id):
    post = Post.objects.filter(id=id).first()
    thispost = get_object_or_404(Post, id=id)
    total_likes = thispost.total_likes()
    liked = False

    if thispost.likes.filter(id=response.user.id).exists():
        liked = True

    context = {
    "post": post,
    "total_likes": total_likes,
    "liked": liked}
    return render(response, "main/post_view.html", context)

def download(response, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fp:
            response = HttpResponse(fp.read(), content_type="application/adminupload")
            response["Content-Disposition"] = 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


@login_required
def post(response):
    form = PostCreateForm()
    if response.method == "POST":
        form = PostCreateForm(response.POST, response.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            title = form.cleaned_data.get("title")
            Post.objects.create(title=title, image=image, author=response.user)
            messages.success(response, "Image Uploaded Succesfully!")
            return redirect('home')

    context = {
        "form": form
    }
    return render(response, "main/new_post.html", context)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "main/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
    
    success_url = reverse_lazy('home')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    template_name = "main/post_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "main/post_update.html"
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False