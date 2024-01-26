from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def index(request):
    return render(request,'index.html')

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
