from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import Image,Comment
from .forms import CommentForm
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required


def index(request):
  title = 'welcome'
  images = Image.all_images()
  context = {
    "title":title,
    "images":images
  }
  return render(request,'index.html',context)

class PostListview(LoginRequiredMixin,ListView):
  model = Image
  template_name = 'index.html'
  context_object_name = 'images'
  ordering = ['-post_date']
  
  
@login_required
def one_image(request,image_id):
  image = Image.objects.get(pk=image_id)
  comments = Comment.image_comments(image_id)
  title = f'image.image_name'
  print(comments)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      Comment.image=image
      print(image_id)
      form.save()
      return redirect('index')
  else:
    form = CommentForm()
  context = {
    "image":image, 
    "title":title, 
    "comments":comments, 
    "commentform":form
    }
  return render(request,'all-image/image_details.html',context)


class PostCreateview(LoginRequiredMixin,CreateView):
  model = Image
  fields = ['image','image_caption']
  
  def form_valid(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class PostUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  model = Image
  fields = ['image','image_caption']
  
  def form_valid(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False
  
class PostDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  model = Image
  success_url = '/'
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False
 