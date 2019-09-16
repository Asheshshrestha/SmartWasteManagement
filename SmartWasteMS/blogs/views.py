from django.shortcuts import render
from blogs.models import Blogs
from blogs.forms import BlogCreationForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


# Create your views here.
class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blogs
    template_name = "blogs/create_blogs.html"
    form_class = BlogCreationForm
    success_url='/'


    def form_valid(self, form):
        blogs = form.save(commit=False)
        blogs.author =self.request.user
        blogs.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(BlogCreateView, self).form_invalid(form)
    

def Display_blogs(request):
    blogs = Blogs.objects.all()
    template_name = "blogs/blog_list.html"

    return render(request,template_name,{'blogs':blogs})