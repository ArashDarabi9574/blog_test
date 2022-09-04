from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.


class IndexView(TemplateView):
    '''
    a class-based-view to show index page
    '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Arash"
        context["posts"] = Post.objects.all()
        return context


class PostListView(ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'posts'
    ordering = '-id'


class PostDetialView(DetailView):
    model = Post


class PostCreateView(CreateView):
   model = Post
   form_class = PostForm
   success_url = '/blog/post/'

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'