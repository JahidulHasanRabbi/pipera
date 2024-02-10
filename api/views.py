from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from .models import BlogModel
from django.shortcuts import redirect

# Create your views here.

class BlogListView(ListView):
    def get(self, request):
        blog = BlogModel.objects.all()
        return render(request, 'index.html', {'blogs': blog})


class BlogCreateView(CreateView):
    model = BlogModel
    fields = ['title', 'content']
    template_name = 'blog_create.html'
    success_url = '/'

class AddBlogView(CreateView):
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog = BlogModel(title=title, content=content)
        blog.save()
        return redirect('home')

class BlogDeleteView(DeleteView):
    def get(self, request, pk):
        blog = BlogModel.objects.get(pk=pk)
        blog.delete()
        return redirect('home')